from apiclient import discovery
from google.oauth2 import service_account
import google_auth_oauthlib

from oauth2client.service_account import ServiceAccountCredentials
from httplib2 import Http

"""
TODO:
	follow: https://www.geeksforgeeks.org/get-list-of-files-and-folders-in-google-drive-storage-using-python/
	pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
"""
# def auth():


def main():
	credentialsPath = './client_secrets.json'

	#View metadata for files in your Google Drive
	#View the photos, videos and albums in your Google Photos
	#See and download all your Google Drive files
	scope = "https://www.googleapis.com/auth/drive.readonly"
	# , \
	# 	"https://www.googleapis.com/auth/drive",\
	# 	"https://www.googleapis.com/auth/drive.metadata.readonly",\
	# 	"https://www.googleapis.com/auth/drive.photos.readonly",\
	
	try:
		credentials = ServiceAccountCredentials.from_json_keyfile_name(credentialsPath, scope)
		http_auth = credentials.authorize(Http())
		drive = discovery.build('drive', 'v3', http=http_auth)

		# Call the Drive v3 API
		results = drive.files().list(
				pageSize=10, fields="nextPageToken, files(id, name)"
			).execute()
		
		items = results.get('files', [])

		if not items:
			print('No files found.')
			return
		print('Files:')
		for item in items:
			print(u'{0} ({1})'.format(item['name'], item['id']))
	except:
		print("fail")


if __name__ == '__main__':
	main()
