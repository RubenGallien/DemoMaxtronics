# DemoMaxtronics

A simple demo project for Maxtronics.

## 🚀 Getting started

First, clone the project and set your Mistral API key:

```bash
export API_KEY=[your_mistral_api_key]
```

Then, get the current project path:

```bash
echo $PWD
```

Append `/helloChoregraph/behavior_1` to the path returned by `echo $PWD`, and save the resulting path somewhere. You will need it later.

### 1. Build the project

Run:

```bash
make
```

### 2. Create a patient file

You can now create a patient file by opening:

http://localhost:5001

When creating the patient file, set the **project path** to the path you saved in the previous step.

### 3. Run the Choregraphe project

1. Import your Choregraphe project.
2. Connect your robot.
3. Open the **ASK_AI** box.
4. Go to **line 52**.
5. Replace `localhost` with the **FLASK IP ADRESS**.
6. Run the project.

> ⚠️ **Important:** Make sure to use the flask's IP address instead of `localhost` in the `ASK_AI` box.

