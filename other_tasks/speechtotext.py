def transcribe_gcs(gcs_uri):
    """Asynchronously transcribes the audio file specified by the gcs_uri."""
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    client = speech.SpeechClient()

    audio = types.RecognitionAudio(uri=gcs_uri)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=16000,
        language_code='en-US')

    operation = client.long_running_recognize(config, audio)

    print('Waiting for operation to complete...')
    response = operation.result(timeout=3600)

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    with open("output.txt", "w", encoding="utf-8") as outp:
        for result in response.results:
            # The first alternative is the most likely one for this portion.
            # transcript = u'Transcript: {}'.format(result.alternatives[0].transcript)
            # confidence = 'Confidence: {}'.format(result.alternatives[0].confidence)
            # print(transcript)
            # print(confidence)
            print(type(result))
            print(result)
            #outp.write(transcript + "\n")
            #outp.write(confidence + "\n")

def transcribe_file(speech_file):
    """Transcribe the given audio file."""
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    client = speech.SpeechClient()

    with io.open(speech_file, 'rb') as audio_file:
        content = audio_file.read()

    audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        language_code='zh-TW')

    response = client.recognize(config, audio)
    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        print(u'Transcript: {}'.format(result.alternatives[0].transcript))            

if __name__ == "__main__":
    import io 
    
    #gcs_uri = "gs://writepath-experimental/hk-audio.mp3"
    #transcribe_gcs(gcs_uri)
    speech_file = "guotaiming-0.flac"
    transcribe_file(speech_file)