
# CosmosHashLib

A simple hashing wrapper with support for salts and peppers

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install CosmosHashLib.

```bash
pip install CosmosHashLib
```

## Usage

```python
import CosmosHashLib

CosmosHashLib.RandLen(73415123615248374531263482374652358413461324623874189024189236192837189237273452631741)
CosmosHashLib.Pepper('secret pepper')

# returns string with hash and salts
# in format salt1$hash$salt2
# '9629480548280199683952534504439555097095034673943361626777618263219601140700721613182$df85bca92a6b4b87abda9e621aa5e662113b4fcbb0c022963e43c3b43a230956$4797f1dbb71ac12b5d8985421ed5b743879e1aba11a2beeab9c39b47c96d94fe'
hash = CosmosHashLib.SHA256.HashSaltPepper('hash a string')

# returns True or False
CosmosHashLib.SHA256.VerifySaltPepper('hash a string', hash)

# Use CosmosHashLib.SHA1 for SHA1 hashes
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)