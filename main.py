#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi
from caesar import encrypt

page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Rot13</title>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h1>
        <a href="/">Rot13</a>
    </h1>
"""
page_footer = """
</body>
</html>
"""

class Index(webapp2.RequestHandler):
    def get(self):

        main_header = "<h2>Input text for Rot 13</h2>"

        text_form = """
        <form action="/rotate" method="post">
            Rotate by how many characters?<br>
            <input type="number" name="rotate_by_number" value="0"/><br><br>
            <textarea name="submitted_text" style="height: 100px; width: 400px;"></textarea>
            <br>
            <input type="submit"/>
        </form>
        """

        error = self.request.get("error")
        error_element = "<p class='error'>" + error + "</p>" if error else ""

        main_content = main_header + text_form + error_element
        response = page_header + main_content + page_footer
        self.response.write(response)

class Rot_13(webapp2.RequestHandler):
    def post(self):

        submitted_text = self.request.get("submitted_text")
        rotate_by_number = int(self.request.get("rotate_by_number"))

        if (submitted_text == ""):
            error = "You didn't enter anything!"
            self.redirect("/?error=" + error)
            return

        rotated_text = encrypt(submitted_text, rotate_by_number)

        main_header = "<h2>Input text for Rot 13</h2>"

        text_form = """
        <form action="/rotate" method="post">
            Rotate by how many characters?<br>
            <input type="number" name="rotate_by_number" value="0"/><br><br>
            <textarea name="submitted_text" style="height: 100px; width: 400px;">""" + rotated_text + """</textarea>
            <br>
            <input type="submit"/>
        </form>
        """

        main_content = main_header + text_form
        response = page_header + main_content + page_footer
        self.response.write(response)

app = webapp2.WSGIApplication([
    ('/', Index),
    ('/rotate', Rot_13)
], debug=True)
