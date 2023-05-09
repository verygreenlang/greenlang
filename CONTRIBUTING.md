# Contributing

We would ❤️ it if you contributed to the project and helped make FINGREEN AI even better. We will make sure that contributing is easy, enjoyable. All contributions are welcome, including features, issues, documentation, guides, and more.

## Got a question?

You can ask questions on our [slack](https://fingreenai.slack.com)

## Found a bug? or Missing a feature?

If you find a bug in the source code, [submitting an issue](https://github.com/fingreen-ai/back/issues/new) to our GitHub Repository.

## Missing a feature?

You can request a new feature by [submitting an issue](https://github.com/amplication/amplication/issues/new?assignees=&labels=type%3A%20feature%20request&template=feature_request.md&title=) to our GitHub Repository.

If you'd like to implement a new feature, it's always good to be in touch with us before you invest time and effort, since not all features can be supported.

- For a Major Feature, first open an issue and outline your proposal. This will let us coordinate efforts, prevent duplication of work, and help you craft the change so that it's successfully integrated into the project.
- Small Features can be crafted and directly [submitted as a Pull Request](#submit-pr).

## What do you need to know to help?


- [django](https://https://www.djangoproject.com/)
- [django rest framework ](https://www.django-rest-framework.org/)
- [pytest](https://docs.pytest.org/en/7.1.x/) (for testing)

# <a name="submit-pr"></a> How do I make a code contribution?

## Step 1:  Clone the repository to your local machine

```
git clone git@github.com:fingreen-ai/back.git

```


## Step2: Prepare the development environment

Set up and run the development environment on your local machine:

**BEFORE** you run the following steps make sure:
1. You have conda installed locally on you machine ```https://www.anaconda.com/download/```
2. You are in a specific conda env ```conda create --name fback ; conda activate fback```

```shell
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
cd back
pip install -r requirements.txt
pre-commit install
pre-commit install --hook-type commit-msg
./tools/migrate.sh
./tools/start.sh
```

## Step 3: Create a branch

Create a new branch for your fix/feature.

```shell
git checkout -b issue/<issue_id>
```

## Step 4: Make your changes

Update the code with your bug fix or new feature.

## Step 5: Add the changes that are ready to be committed

Stage the changes that are ready to be committed:

```shell
git add .
```

## Step 6: Commit the changes and fight with pre-commit hooks

First loop with this command
```shell
git add .; git commit -m "test"
```
Then when the precommit hook only show the commit message error, commit with :
```shell
cz commit
```


## Step 7: Push the changes to the remote repository

Push the changes to the remote repository using:

```jsx
git push origin issue/<issue_id>
```

## Step 8: Create Pull Request to preprod

In GitHub, do the following to submit a pull request to the upstream repository:

1.  Give the pull request a title and a short description of the changes made. Include also the issue or bug number associated with your change. Explain the changes that you made, any issues you think exist with the pull request you made, and any questions you have for the maintainer.

Remember, it's okay if your pull request is not perfect (no pull request ever is). The reviewer will be able to help you fix any problems and improve it!

2.  Wait for the pull request to be reviewed by a maintainer.

3.  Make changes to the pull request if the reviewing maintainer recommends them.

🎉🎉🎉 Celebrate your success after your pull request is merged 🎉🎉🎉
