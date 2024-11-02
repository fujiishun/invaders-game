from flask import Blueprint, Response
from ..components.top import generate_frame

video_feed = Blueprint("video_feed", __name__)

@video_feed.route("/video_feed")
def video_feed_route():
    return Response(generate_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')
