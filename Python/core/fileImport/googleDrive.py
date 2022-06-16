from apiclient import discovery
from oauth2client.service_account import ServiceAccountCredentials
from httplib2 import Http

def main():
	credentialsPath = 'core/fileImport/client_secrets.json'

	#See and download all your Google Drive files
	scope = "https://www.googleapis.com/auth/drive.readonly"
	
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
		print("Failed to retrieve files. Refer to the following articles for troubleshooting:")
		print("\thttps://developers.google.com/drive/api/v3/quickstart/python")
		print("\thttps://www.geeksforgeeks.org/get-list-of-files-and-folders-in-google-drive-storage-using-python/")


if __name__ == '__main__':
	main()
