
youtubeApi = "https://www.googleapis.com/youtube/v3/captions?part=snippet&videoId=_9-ajTbM838"
client = "711701825464-3pi8p8bb9al6gqdcrhkbcinm16gii4t7.apps.googleusercontent.com"

def captions_list(client, **kwargs):
  # See full sample for function
  kwargs = remove_empty_kwargs(**kwargs)

  response = client.captions().list(
    **kwargs
  ).execute()

  return print_response(response)

captions_list(client,
    part='snippet',
    videoId='M7FIvfx5J10',
    onBehalfOfContentOwner='')
