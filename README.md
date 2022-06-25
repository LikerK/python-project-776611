### Hexlet tests and linter status:
[![Actions Status](https://github.com/LikerK/python-project-lvl4/workflows/hexlet-check/badge.svg)](https://github.com/LikerK/python-project-lvl4/actions)
[![Linter CI](https://github.com/LikerK/python-project-lvl4/actions/workflows/my_linter.yml/badge.svg)](https://github.com/LikerK/python-project-lvl4/actions/workflows/my_linter.yml)

---
## Description

**Task Manager** is a task management system. It allows you to set tasks, assign performers and change their statuses. Registration and authentication are required to work with the system.

---
## Deployment

**Task manager** is deployed on heroku, you can go and test this project.

[![Heroku](https://pyheroku-badge.herokuapp.com/?app=immense-wave-07675&style=flat)](https://immense-wave-07675.herokuapp.com)

---
## How to run a project locally

#### 1. Clone the repository
<code>$ pip install --user git+https://github.com/LikerK/python-project-lvl4.git</code>

#### 2. Create an environment variable

<code>Create .evn file in your project and put your environment variables there. You can see an example in the evn.exemple file.</code>

#### 3. Install poetry

<code>$ make install</code>

#### 4. Make migrate

<code>$ make migrations </code>

#### 5. Run sever

<code>$ make runserver </code>
