from flaskBlog import app,bcrypt,db
from flask import render_template, url_for,flash,redirect,request
from flaskBlog.forms import Loginform,Registrationform,UpdateAccountform,PostForm
from flaskBlog.modules import User,Post
from flask_login import login_user,current_user,logout_user,login_required


@app.route("/")
@app.route("/home")
def home():
    posts= Post.query.all()
    return render_template('home.html',title="Home",posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title="About")

@app.route("/register",methods=["POST","GET"])
def register():
    if current_user.is_authenticated:
        flash(f'Already Logged In','success')
        return redirect(url_for('home'))
    form = Registrationform()
    if form.validate_on_submit():
        hpassword = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,email=form.email.data,password=hpassword)
        db.session.add(user)
        db.session.commit()
        flash(f'Account registered successfully for { form.username.data }!','success')
        return redirect(url_for('login'))
    return render_template('register.html', title="Register",form=form)

@app.route("/login",methods=["POST","GET"])
def login():
    if current_user.is_authenticated:
        flash(f'Already Logged In','success')
        return redirect(url_for('home'))
    form = Loginform()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            flash(f'Authenticated Successfull','success')
            next_page=request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash(f'Email or Password Incorrect, Retry','danger')
            return redirect(url_for('login'))
    return render_template('login.html', title="Login",form=form)


@app.route("/logout")
def logout():
    logout_user()
    flash(f'Logged Out Successfully','success')
    return redirect(url_for('home'))

@app.route("/account",methods=["POST","GET"])
@login_required
def account():
    image_file = url_for('static',filename=current_user.username + '.jpg')
    form = UpdateAccountform()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash(f'Account Updated Successfully','success')
        return redirect(url_for('account'))
    # if current_user.is_authenticated:
    #     return redirect(url_for('home'))
    return render_template('account.html',title="Account",image_file=image_file,form=form)

@app.route("/post/new",methods=["POST","GET"])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data,content=form.content.data,author=current_user.username)
        db.session.add(post)
        db.session.commit()
        flash(f'New Post Created','success')
        return redirect(url_for('home'))
    return render_template('new_post.html',title="New Post",form=form)