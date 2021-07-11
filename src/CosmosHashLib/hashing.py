import hashlib
import random

pepper = False
maxRandLen = 7341512361524837453126348237465235841

def RandLen(integer):
    global maxRandLen
    maxRandLen = int(integer)

def Pepper(string):
    global pepper
    pepper = string

class SHA256:
    def HashSaltPepper(string):
        global pepper
        global maxRandLen
        if pepper != False:
            salt = str(random.SystemRandom().randint(0, maxRandLen))
            saltt = str(random.SystemRandom().randint(0, maxRandLen))
            saltt = hashlib.sha256(saltt.encode()).hexdigest()
            string = pepper + salt + string + pepper + salt + saltt
            encoded = string.encode()
            result = hashlib.sha256(encoded)
            return f'{salt}${result.hexdigest()}${saltt}'
        else:
            salt = str(random.SystemRandom().randint(0, maxRandLen))
            saltt = str(random.SystemRandom().randint(0, maxRandLen))
            saltt = hashlib.sha256(saltt.encode()).hexdigest()
            string = salt + string + salt + saltt
            encoded = string.encode()
            result = hashlib.sha256(encoded)
            return f'{salt}${result.hexdigest()}${saltt}'
        
    def VerifySaltPepper(string, hash):
        global pepper
        global maxRandLen
        if pepper != False:
            if (len(hash.split('$')) == 3):
                salt = hash.split('$')[0]
                saltt = hash.split('$')[2]
                string = pepper + salt + string + pepper + salt + saltt
                encoded = string.encode()
                result = hashlib.sha256(encoded)
                result = f'{salt}${result.hexdigest()}${saltt}'
                if (result == hash):
                    return True
                else:
                    return False
            else:
                return False
        else:
            if (len(hash.split('$')) == 3):
                salt = hash.split('$')[0]
                saltt = hash.split('$')[2]
                string = salt + string + salt + saltt
                encoded = string.encode()
                result = hashlib.sha256(encoded)
                result = f'{salt}${result.hexdigest()}${saltt}'
                if (result == hash):
                    return True
                else:
                    return False
            else:
                return False
            
class SHA1:
    def HashSaltPepper(string):
        global pepper
        global maxRandLen
        if pepper != False:
            salt = str(random.SystemRandom().randint(0, maxRandLen))
            saltt = str(random.SystemRandom().randint(0, maxRandLen))
            saltt = hashlib.sha1(saltt.encode()).hexdigest()
            string = pepper + salt + string + pepper + salt + saltt
            encoded = string.encode()
            result = hashlib.sha1(encoded)
            return f'{salt}${result.hexdigest()}${saltt}'
        else:
            salt = str(random.SystemRandom().randint(0, maxRandLen))
            saltt = str(random.SystemRandom().randint(0, maxRandLen))
            saltt = hashlib.sha1(saltt.encode()).hexdigest()
            string = salt + string + salt + saltt
            encoded = string.encode()
            result = hashlib.sha1(encoded)
            return f'{salt}${result.hexdigest()}${saltt}'
        
    def VerifySaltPepper(string, hash):
        global pepper
        global maxRandLen
        if pepper != False:
            if (len(hash.split('$')) == 3):
                salt = hash.split('$')[0]
                saltt = hash.split('$')[2]
                string = pepper + salt + string + pepper + salt + saltt
                encoded = string.encode()
                result = hashlib.sha1(encoded)
                result = f'{salt}${result.hexdigest()}${saltt}'
                if (result == hash):
                    return True
                else:
                    return False
            else:
                return False
        else:
            if (len(hash.split('$')) == 3):
                salt = hash.split('$')[0]
                saltt = hash.split('$')[2]
                string = salt + string + salt + saltt
                encoded = string.encode()
                result = hashlib.sha1(encoded)
                result = f'{salt}${result.hexdigest()}${saltt}'
                if (result == hash):
                    return True
                else:
                    return False
            else:
                return False