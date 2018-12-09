from django.shortcuts import render, reverse, HttpResponseRedirect, redirect

###################      youtube           #######################
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

'''
import os

import flask

import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery

# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret.
CLIENT_SECRETS_FILE = "\client_secrets.json"

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account and requires requests to use an SSL connection.
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

app = flask.Flask(__name__)

with app.app_context():
    # within this block, current_app points to app.
    print (flask.current_app.name)


# Note: A secret key is included in the sample so that it works, but if you
# use this code in your application please replace this with a truly secret
# key. See http://flask.pocoo.org/docs/0.12/quickstart/#sessions.
app.secret_key = os.urandom(24)


if __name__ == '__main__':
  # When running locally, disable OAuthlib's HTTPs verification. When
  # running in production *do not* leave this option enabled.
  os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
  app.run('localhost', 8090, debug=True)


def my_url_for(*args, **kwargs):
    with app.test_request_context():
        # With the test request context of the app
        kwargs['_external'] = True    # Add the _external=True keyword argument to whatever else was passed
        url = flask.url_for(*args, **kwargs)    # Get the URL
        PORT = 8000
        url = url.replace('://localhost/', '://localhost:%d/' % (PORT))    # Oh yeah, add the port to the URL!
        # I only need to add the port to when I'm running locally, but you could use a regex here to add the port to any servername, if you have that type of setup

        return url



def index(request):
    print("1")
    with app.test_request_context():

      if 'credentials' not in flask.session:
        print("2")
        return redirect(flask.url_for('authorize'))

      print("3")
      # Load the credentials from the session.
      credentials = google.oauth2.credentials.Credentials(
          **flask.session['credentials'])
      print("4")
      client = googleapiclient.discovery.build(
          API_SERVICE_NAME, API_VERSION, credentials=credentials)
      print("5")
      return channels_list_by_username(client,
        part='snippet,contentDetails,statistics',
        forUsername='GoogleDevelopers')


@app.route('/Video/authorize')
def authorize(request):

  with app.test_request_context():
      # Create a flow instance to manage the OAuth 2.0 Authorization Grant Flow
      # steps.
      print("A")
      flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(CLIENT_SECRETS_FILE, scopes=SCOPES)
      print("B")
      flow.redirect_uri = my_url_for('oauth2callback')
      print("C")
      authorization_url, state = flow.authorization_url(
          # This parameter enables offline access which gives your application
          # both an access and refresh token.
          access_type='offline',
          # This parameter enables incremental auth.
          include_granted_scopes='true')
      print("D")
      # Store the state in the session so that the callback can verify that
      # the authorization server response.
      flask.session['state'] = state
      print("E")
      return redirect(authorization_url)


@app.route('/Video/oauth2callback')
def oauth2callback(request):
    with app.test_request_context():
        print("a")
        # Specify the state when creating the flow in the callback so that it can
        # verify the authorization server response.
        state = flask.session['state']
        print("b")
        flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file( CLIENT_SECRETS_FILE, scopes=SCOPES, state=state)
        print("c")
        flow.redirect_uri = flask.url_for('oauth2callback', _external=True)
        print("d")
        # Use the authorization server's response to fetch the OAuth 2.0 tokens.
        authorization_response = flask.request.url
        print("dd")
        print(flask.request_url)
        flow.fetch_token(authorization_response=authorization_response)
        print("e")
        # Store the credentials in the session.
        # ACTION ITEM for developers:
        #     Store user's access and refresh tokens in your data store if
        #     incorporating this code into your real app.
        credentials = flow.credentials
        flask.session['credentials'] = {
                  'token': credentials.token,
                  'refresh_token': credentials.refresh_token,
                  'token_uri': credentials.token_uri,
                  'client_id': credentials.client_id,
                  'client_secret': credentials.client_secret,
                  'scopes': credentials.scopes
        }
        print("f")
        return redirect(flask.url_for('index'))



def channels_list_by_username(client, **kwargs):
  response = client.channels().list(
    **kwargs
  ).execute()

  return flask.jsonify(**response)


###################      youtube           #######################
'''

# 비디오 메인 페이지 테스트
def Test_VideoMain(request):

    return render(request, 'TestVideoMain.html')


def download_caption(youtube, **kwargs):

  kwargs = remove_empty_kwargs(**kwargs)

  subtitle = youtube.captions().download(
    **kwargs
  ).execute()

  print ("First line of caption track: %s" % (subtitle))

  return subtitle


def Test_VideoCaption(request):



    return render(request, 'TestVideoCaption.html', {'output' : output})


# /Video/list/
def VideoList(request):

    # 로그인 했을 경우
    if 'userId' in request.session :
        userId = request.session['userId']
        return render(request, 'VideoList.html', {'userId' : userId})

    # 로그인 안했을 경우
    else:
        redirect_to = reverse('Main')
        return HttpResponseRedirect(redirect_to)
