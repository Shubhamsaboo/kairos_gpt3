# Contributing to Kairos GPT-3 Sandbox

Thanks for your interest in contributing to the community driven GPT-3 Sandbox. We're grateful for your initiative! ❤️

We are [Shubham](https://www.linkedin.com/in/shubhamsaboo/) and [Sandra](https://www.linkedin.com/in/sandrakublik/), co-founders of [Kairos Data Labs](https://www.linkedin.com/company/kairos-data-labs). We are very excited to have you here and invite you to contribute towards the development of GPT-3 sandbox to make it accessible and usable for everyone.

In this guide, we'll walk you through ways in which you can contribute.

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [🐞 Bugs and Issues](#-bugs-and-issues)
- [🥇 Adding New Examples](#-adding-new-examples)
- [☑️ Naming Conventions](#-naming-conventions)
- [💥 Testing Sandbox Locally](#-testing-sandbox-locally)
- [📖 Reference Resources](#-reference-resources)
- [🙏 Thank You](#-thank-you)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

<a name="-bugs-and-issues"></a>
## 🐞 Bugs and Issues

### Submitting Issues

We love to get issue reports. But we love it even more, if they're in the right format. For any bugs you encounter, we need you to:

* **Describe your problem**: What exactly is the bug. Be as clear and concise as possible
* **Why do you think it's happening?** If you have any insight, pls share

There are also a couple of nice to haves:

* **Environment:** Specify the python version you are using within your virtual environment
* **Screenshots:** If they're relevant

To understand how our issues are labeled, check out our [issue label guide](.github/github-issue-label-guide.md).

<a name="-adding-new-examples"></a>
## 🥇 Adding New Examples

0. Associate your local git config with your github account. If this is your first time using git you can follow [the steps](#associate-with-github-account).
1. Fork the `kairos_gpt3` repo and clone onto your computer. 
1. Create a [new branch](#naming-your-branch), for example `fix-kairos-1`, `example-kairos-1`
1. Work on this branch to do the fix/improvement or adding a new example
1. If you want to add a new example, you can copy the code from the email_generation folder, modify it as per your use-case and save the folder as `example_name`
1. Commit the changes with the [correct commit style](#writing-your-commit-message).
1. Make a pull request.
1. Request reviews from one of [the repository owners](.github/code_owners).
1. After review 👍 the PR will get merged and you would have successfully contributed to the project!

**Note:** If you're just fixing a typo or grammatical issue, you can go straight to a pull request.

### Associate with Github Account

- Confirm username and email on [your profile page](https://github.com/settings/profile).
- Set git config on your computer.

```shell
git config user.name "YOUR GITHUB NAME"
git config user.email "YOUR GITHUB EMAIL"
```

- (Optional) Reset the commit author if you made commits before you set the git config.

```shell
git checkout YOUR-WORKED-BRANCH
git commit --amend --author="YOUR-GITHUB-NAME <YOUR-GITHUB-EMAIL>" --no-edit
git log  # to confirm the change is effective
git push --force
```

<a name="-naming-conventions"></a>
## ☑️ Naming Conventions

For branches, commits, and PRs we recommend you to follow these basic naming conventions:

* Be descriptive
* Use all lower-case
* Limit punctuation
* Be consise with your description (under ~100 characters is best)
* In general, follow the [Conventional Commit](https://www.conventionalcommits.org/en/v1.0.0/#summary) guidelines

Note: If you don't follow naming conventions, your commit will be automatically flagged to be fixed.

### Naming your Branch

Your branch name should follow the format `type-scope(-issue_id)`:

* `type` is either `example` or `issue`
* `scope` is optional, and represents the example name that your branch is working on or the brief issue name. 
* `issue_id` is [the GitHub issue](https://github.com/Shubhamsaboo/kairos_gpt3/issues) number. Having the correct issue number will automatically link the Pull Request on this branch to that issue.

> Good examples:
>
```text
issue-dashboard_not_loading-127
example-email_assitant
```

> Bad examples:
>

| Branch name     | Feedback                                              |
| ---             | ---                                                   |
| `MYFIX123`      | Not descriptive enough, all caps, doesn't follow spec |
| `mybranch-1`    | Not descriptive                                       |


### Writing your Commit Message

A good commit message helps us track the development of GPT-3 sanbox. A Pull Request with a bad commit message might be *rejected* due to the lack of clarity.

Commit messages should stick to our [naming conventions](#naming-conventions) outlined above, and use the format `type(scope?): subject`:

* `type` is either `example` or `issue`.
* `scope` and represents the example name that your branch is working on or the brief issue name.
* `subject` should explains the commit in a brief and descriptive way

For example, a commit message that includes a new example should be phrased as: `example(email_assistant): Added new example application - GPT-3 powered Email Assistant`


### Naming your Pull Request

We don't enforce naming of PRs and branches, but we recommend you follow the same style as the commit naming convention to make it easy for the community to follow up on the new developments. It can simply be one of your commit messages, just copy/paste it, e.g.  `example(email_assistant): Added new example application - GPT-3 powered Email Assistant`.

<a name="-testing-sandbox-locally"></a>
## 💥 Testing GPT-3 Sandbox Locally

You need to have python 3.7+ installed, and then you can create a python virtual environment using [pip](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) or [conda](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activating-an-environment) depending on your python setup. 

After installing and activating the virtual environment (The commands will differ for windows and linux installations which is clearly specified in the respective documentations), you can `cd` into the email_generation folder:

```bash
cd email_generation
```

From `/email_generation` folder, you can run the following command to install the required dependencies

```bash
pip install -r requirements.txt
```

After installing the required dependencies, you can bring up the main application to validate that its working in your local enviroment. To bring up the application, you can run the following command from the `email_generation` folder.

```bash
streamlit run gpt_app.py
```

<a name="-referecnce-resources"></a>
## 📖 Reference Resources

For your reference, we have created example applications to take inspiration from and come up with new ideas that can be useful for the developer community.

* [GPT-3 Applications](https://shubhamsaboo111.medium.com/) 
* [Video Tutorials/examples](https://www.youtube.com/channel/UCjG6QzmabZrBEeGh3vi-wDQ)


## 🙏 Thank You

Thanks so much for your interest in contributing to this sandbox. We're excited to see your contributions!
