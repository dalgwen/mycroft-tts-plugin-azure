### mycroft-tts-plugin-azure

This TTS service for Mycroft requires a subscription to Microsoft Azure and the creation of a Speech resource (https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/overview#create-the-azure-resource)

The free plan is more than capable to handle domestic usage (5 million character per month, or 0.5 million with neural tts)
You can choose your voice here in the column "voice name" (https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support#text-to-speech)

New configuration (only the api_key is mandatory, other are defaulted as in the following) :

```json
"tts": {
    "module": "azure",
    "azure": {
        "api_key": "insert_your_key_here",
        "voice": "en-US-JennyNeural",
        "region": "westus"
    }
}
```

##### LICENSE :

Apache-2.0