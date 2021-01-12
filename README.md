# Explory
Explorer sort/system application


Ich habe Visual Studio Code benutzt. 
https://code.visualstudio.com

Visual Studio Code Extentions:
- Prettier		
https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode
- Git Graph	
https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph
- GitHub Actions
https://marketplace.visualstudio.com/items?itemName=cschleiden.vscode-github-actions
- Mocha Test Explorer	
https://marketplace.visualstudio.com/items?itemName=hbenl.vscode-mocha-test-adapter

Installation:
- Zuerst muss man Python installieren: https://www.python.org/downloads/
- py -3 -m venv venv   --> stellt ein Environment her
- venv\Scripts\activate	 --> Environment staten
- python -m pip install pyqt5-tools	--> PyQt5 installieren https://pypi.org/project/PyQt5/
- python -m pip install pyinstaller -->	Pyinstaller instalieren https://www.pyinstaller.org
- python -m pip install pylint		-- >pylint installieren https://pypi.org/project/pylint/
- python -m pip install mypy	-->	mypy installieren https://pypi.org/project/mypy/

Build:
- build: pyinstaller explory/explory.py	-->Pyinstaller build https://www.pyinstaller.org
- pylint: pylint explor/explory.py	-->	pylint starten
- mypy: mypy explory/explory.py	 --> mypy starten
