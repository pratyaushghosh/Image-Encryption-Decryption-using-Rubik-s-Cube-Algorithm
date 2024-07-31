import firebase_admin, datetime
from firebase_admin import credentials, db


def getDatabase():
    if not firebase_admin._apps:
        cred = credentials.Certificate('cred.json')
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://image-cryptography-default-rtdb.firebaseio.com/'
        })
        database = db.reference()
        print(database)
        return database


def pushData():
    with open('image_id.txt') as id:
        imgIdValue = id.read()
    print(imgIdValue)

    with open('gmail_id.txt') as email:
        emailIdValue = email.read()

    with open('phone_no.txt') as mobileNo:
        mobileNoValue = mobileNo.read()
    print(mobileNoValue)

    with open('password.txt') as Pass:
        PasswordValue = Pass.read()
    print(PasswordValue)

    with open('securitycode.txt') as otp:
        SecurityCodeValue = otp.read()
    print(SecurityCodeValue)

    if not firebase_admin._apps:
        database = getDatabase()

        # image id
        imgId = database.child('ImageId')
        imgId.update({
            imgIdValue : imgIdValue
        })

        #email
        emailId = database.child('EmailId')
        emailIdKey = imgIdValue
        emailId.update({
            emailIdKey : emailIdValue
        })

        #Mobile No
        mobileNo = database.child('MobileNo')
        mobileKey = imgIdValue
        mobileNo.update({
            mobileKey : mobileNoValue
        })

        #password
        Password = database.child('Password')
        PasswordKey = imgIdValue
        print(PasswordKey)
        Password.update({
            PasswordKey: PasswordValue
        })

        #SecurityCode
        SecurityCode = database.child('SecurityCode')
        SecurityCodeKey = imgIdValue
        SecurityCode.update({
            SecurityCodeKey: SecurityCodeValue
        })

        #Datetime
        DateTime = database.child('DateTime')
        DateTimeValue = str(datetime.datetime.now())
        DateTimeKey = imgIdValue
        DateTime.update({
            DateTimeKey: DateTimeValue
        })

def fetchData(imgId, Password, securityCode):
    if not firebase_admin._apps:
        database = getDatabase()
        imageId = database.child('ImageId').get()
        password = dict(database.child('Password').get())
        SecurityCode = dict(database.child('SecurityCode').get())
        if(imgId in imageId):
            if(Password == password.get(imgId)):
                if(securityCode == SecurityCode.get(imgId)):
                    print(True)
                    firebase_admin._apps.clear()
                    return True
                else:
                    print('OTP not Matched...Reenter the OTP')
                    firebase_admin._apps.clear()
                    return False
            else:
                print('Password not Matched...Reenter the Password')
                firebase_admin._apps.clear()
                return 'password Not Matched'
        else:
            print('Image Id not Matched...Reenter the Image Id')
            firebase_admin._apps.clear()
            return 'imgId Not Matched'

def checkImgId(imgId):
    if not firebase_admin._apps:
        database = getDatabase()
        imageId = database.child('ImageId').get()
        if(imgId in imageId):
            print(True)
            firebase_admin._apps.clear()
            return True

#print(checkImgId('IMG_88'))
#print(fetchData('IMG_88', '123', 'umR5nNkjP4'))
#print(fetchData('IMG_88', '125', 'umR5nNkjP4'))





