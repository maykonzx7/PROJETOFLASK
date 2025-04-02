from flask import Blueprint, render_template

thanks_route = Blueprint ('thanks', __name__)

@thanks_route.route ('/thanks')
def thanks ():
    return render_template('thanks.html')