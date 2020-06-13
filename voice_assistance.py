import speech_recognition as sr

json_string = '''
{
  "type": "service_account",
  "project_id": "divine-aegis-273407",
  "private_key_id": "532f45235374478c5431cc563d97eb8948656c70",
  "private_key": "MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQClHuRDGP71I2uLz8QKDlZv8iX+IrmnXWfHvi3/Q/nQM0x5cwnoGQnjSmHGPW03aydnkrtshJVWGDE22RA+VHM+xCE+9fLPei5kFiHVznfdwd0fQ5qE16tHvhnBuODDOyBXIuLxukStMssdBs3Fs1CLZ0f8PW/KKi6cHhL4RP7HKLY97MKXL0f4/j9L3mZ1OGQ/vWfVOanuPxWHdJtHEQ5Hpdw72WJLqL9vuyu/IzEwOCb2LOnz5/5c9JpRQ6bvDzl0Je1IIOzygQGAVYpdQZ4b7u9FZt2BG1mmSK6tDMgOu1Niwi5EikVvn9DmI/ubDLR8z/+VOnVndU7vH7K/RrBNAgMBAAECggEAER1vmYjYvH4MYrSJZGVyDi5yQ7JDvhZPcIPE7sWT+kGm9pu29ijKPpXyJoMtc+YWcoTiCnB/rinZyA6dwWgtfd8Edys1HM5USqmEnk3FXOYAToJKXOSh61DICK1qFrJlOsLx9Q5SmgU+ymZvI8PfYGO3MW0IzlKq/CGd47/7DJd/9EeoZ2QUapZQEebCfkkprGC6cyzGjuDb2vjac3TyS48erO95CQJeGqnCWuMfeIVnguk9WhvRQJKq0l4qWT7OaX4hVYLvgWhWAcs+nPl51ajrXPwBkomXxIq07hIEFRy1DoyY0pH9ZMC5GZFcGUNVsHXo1hpIpdlgOgBRk1HWIQKBgQDeLnrkfEaMkWZ0KcPBfbOfVP7FLPVBvInAtOfftmrRJgXQ2eRaDEit5uernaDLmNQkBM2WV2C7/3B0weut4G1oOQUX9OLVyujzH9q4jQqKNkiuwlGKGBOYuutbLhzVgvhk3Gcga7wwsd4+T2oU/33ts3VCcPaHScVRLJ22rVXCQKBgQC+QPqHRmsE8Ttc7oSfNRUKt0eDl+ORAbPcn6kbk8fFRw+lFg9hsnXf1in9RO1CgLlwS8RyPkeTfgBT4BE083x+bMTZj8SeYZEoaOhPVV0D1DrOPW9R+/Ecl/M9mECnNf+r38JA6zAMx7+W4zJ2mnpLbBFEW+/Z9PIMlbKBRM8JQKBgQDQkDEsaryPF65lPQ90/RRBocRD3ZsyTeLiW/Trs9gAvdNHgy6lgHkfbdvXiU4WtmTkK1rdmeX+E+rRF5gOmpRYOz/fIFUkaB+/EyhI3S66pL2vrIN4KE6/RnyVv4kmO4/LoOz1TYc62p0FInKOoMm2zxNI+HGxPcyCWopsp8GygQKBgDN80lAZtoy33CDiS/HqI6+quifayzNLCqoCa3mTHNU+zfUXa0I9Ubkp9GMebDc7LvQ9DQT95dD8oIoScZWq714ngX5/ce6K6QXOnlAaAfovTVrTNXUygaYDWUiqE5Us/+w7ug5nl7FdvXPQOK/wTnhq3qFpYBfUOlna3bH+fZ4hAoGBAL6ozj2/EYoyZlo6fcfncowgxPoIsthJJIMxTL9R7VK3CpK5u3JKD2W/Grm1UTTjfvqayGJaqB0fYFcD7tnkS/5q1I88vTwt0yIm8CnHUnpPEa+Fd2ij9Gp5VLKmBg7N5Lr424UEHCIarWu9LmrRMAM4Q9FwqXZ7JaSK9FAGMdYv",
  "client_email": "cloud-vision@divine-aegis-273407.iam.gserviceaccount.com",
  "client_id": "100049148430509442181",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/cloud-vision%40divine-aegis-273407.iam.gserviceaccount.com"
}
'''
r = sr.Recognizer()
m = sr.Microphone()

try:
    print("A moment of silence, please...")
    with m as source: 
        r.adjust_for_ambient_noise(source)

    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    while True:
        print("Say something!")
        with m as source: audio = r.listen(source)
        print("Got it! Now to recognize it...")
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)
            
            # we need some special handling here to correctly print unicode characters to standard output
            if str is bytes:  # this version of Python uses bytes for strings (Python 2)
                print(u"You said {}".format(value).encode("utf-8"))
            else:  # this version of Python uses unicode for strings (Python 3+)
                print("You said {}".format(value))
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
except KeyboardInterrupt:
    pass