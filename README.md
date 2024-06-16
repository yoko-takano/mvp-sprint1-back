# mvp-sprint1-back

This repository contains the backend source code for the MVP of the Basic Full Stack Development sprint.

## Sumary

1. [Description](#1-description)
2. [Technologies](#2-technologies)
3. [How To](#3-how-to)

## 1. Description

According to the [OPC Foundation](https://reference.opcfoundation.org/I4AAS/v100/docs/4.1), the Asset Administration Shell (AAS) is the standardized digital representation of an asset in Industry 4.0. This representation not only encapsulates the physical data of an asset but also integrates its operational logic and evolutionary history. In a scenario where digitization and connectivity are essential, the AAS becomes crucial for interoperability between systems, enabling different components of a smart factory to communicate efficiently and adapt to real-time operational changes.

The AAS goes beyond just a static description of an asset. It is dynamic, continuously updated by system designers, asset users, applications, and processes throughout the asset's lifecycle. This not only enhances operational efficiency but also enables advanced strategies such as predictive maintenance and resource optimization.

In the context of this MVP, the focus is on simplifying the AAS creation process, emphasizing fundamental aspects such as identification, asset type, global information, among others. This serves as a foundational step towards developing more robust capabilities involving detailed submodels and property elements, essential for detailed and intelligent asset management in Industry 4.0.

Building on this initial groundwork, the goal is to expand this project to include advanced functionalities for modeling Asset Administration Shells, supporting a wider variety of asset types and enabling deeper integrations with production and maintenance systems. This effort will not only facilitate the management of complex assets but also promote greater efficiency and adaptability in modern industrial environments.

## 2. Technologies

- `Python`
- `Flask`
- `SQLAlchemy`

## 3. How To

To run this project, you will need to have all Python libraries listed in the `requirements.txt` file installed. Follow the steps below to set up the environment and run the application.

### 3.1. Clone the Repository

Clone the repository to your local environment.

```sh
$ git clone <repository-url>
$ cd mvp-sprint1-back
```

### 3.2. Create and Activate the Virtual Environment

It is recommended to use virtual environments, such as `virtualenv`, to manage project dependencies.

```sh
$ python -m venv env
$ source env/bin/activate  # On Windows use `env\Scripts\activate`
```

### 3.3. Install Dependencies

Install the dependencies listed in the `requirements.txt` file.

```sh
(env)$ pip install -r requirements.txt
```

### 3.4. Running the API

To start the API, execute the command below.

```sh
(env)$ flask run --host 0.0.0.0 --port 5000
```

#### Development Mode

In development mode, it's recommended to use the `--reload` parameter, which will automatically restart the server whenever there is a change in the source code.

```sh
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Open [http://localhost:5000/#/](http://localhost:5000/#/) in your browser to check the status of the running API.
