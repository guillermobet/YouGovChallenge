# YouGov Challenge

## Prerequisites

Before you start, you need to have Python 3 installed on your machine. You can check if you have Python 3 installed by running the following command in your terminal:

```bash
python3 --version
```

If Python 3 is not installed, you can download it from the official website: https://www.python.org/downloads/

## Creating a Virtual Environment

To create a virtual environment, follow these steps:

1. Open your terminal and navigate to the directory where you want to create your virtual environment.

2. Run the following command to create a virtual environment named venv:

```bash
python3 -m venv venv
```

3. Activate the virtual environment by running the following command:

```bash
source venv/bin/activate
```

You should now see '**(venv)**' at the beginning of your command prompt, indicating that you are in the virtual environment.

## Installing Flask

Once you have activated your virtual environment, you can install the required packages for the project by running the following command in your terminal:

```bash
pip3 install -r requirements.txt
```

## Running the Application

Once you have created your virtual environment and installed Flask, you can run the Flask application by running the following command in the temrinal:

```bash
flask run
```

The Flask application should now be running on http://localhost:5000/. You can access it using a web browser or a REST client. For debug mode, just add `--debug` to the command above.

## (Optional) Import Insomnia's request collection

You can perform requests to the endpoints on this project by accessing them through any REST client, in this case a `insomnia.json` file is provided with sample requests.

Make sure you have Insomnia installed, if not you can download it from the official website: https://insomnia.rest/download

Then, import the `insomnia.json` file into Insomnia, this will load a collection of requests called **YouGov Challenge**, click on the collection and you will find four requests

1. Get question - ✅: Given a variable ID, get the associated question's data, including lable, uuid, options and more.
2. Get answer count - ✅: Given a variable ID, get the answer count to the associated question.
3. Get question - ❌: Returns an error given the invalid variable ID
4. Get answer count - ❌: Returns an error given the invalid variable ID

## Considerations

- This app in NOT production-ready.
- This app provides a minimal viable solution to the challenge described in the `Instructions.txt` file, following the recommendations under the `Guidance` section. Major architectural and implementation desicions (e.g. project structure, error handling, modularization, etc) were explicitly left out in favor of a simpler solution to the challenge provided.
- This app is provided under de MIT License.
