### ovos-tts-plugin-azure

This TTS service for OpenVoiceOS requires a subscription to Microsoft Azure and the creation of a Speech resource (https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/overview#create-the-azure-resource)

The free plan is more than able to handle domestic usage (5 million character per month, or 0.5 million with neural tts).
You can choose your voice here in the column "voice name" (https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support#text-to-speech)

Configuration parameters (only the api_key is mandatory, other are defaulted as in the following) :

```json
"tts": {
    "module": "ovos-tts-plugin-azure",
    "ovos-tts-plugin-azure": {
        "api_key": "insert_your_key_here",
        "voice": "en-US-JennyNeural",  # optional, default "en-US-Guy24kRUS"
        "region": "westus" # optional, if your region is westus
    }
}
```

##### Installation

`pip install ovos-tts-plugin-azure`

##### LICENSE :

Apache-2.0
