# Preface

> The vast majority of workloads will go to the cloud. We’re just at the beginning—there’s so much more to happen.
> 
> [Andy Jassy](https://oreil.ly/7Ube0)

Cloud usage has been gaining traction with enterprises and small businesses over the last decade and continues to accelerate. Gartner said the worldwide infrastructure as a service (IaaS) public cloud services market [grew 40.7% in 2020](https://oreil.ly/bJ5Sb). The rapid growth of the cloud has led to a [huge demand](https://oreil.ly/kstre) for cloud skills by many organizations. Many IT professionals understand the basic concepts of the cloud but want to become more comfortable working in the cloud. This gap between the supply and demand of cloud skills presents a significant opportunity for individuals to level up their career.

Through our combined 20+ years of cloud experience, we have had the benefit of working on Amazon Web Services (AWS) projects in many different roles. We have provided guidance to hundreds of developers on how and when to use AWS services. This has allowed us to understand the common challenges and easy wins of the cloud. We would like to share these lessons with you and give you a leg up for your own advancement. We wrote this book to share some of our knowledge and enable you to quickly acquire useful skills for working in the cloud. We hope that you will find yourself using this book as reference material for many years to come.

# Who This Book Is For

This book is for developers, engineers, and architects of all levels, from beginner to expert. Beginners will learn cloud concepts and become comfortable working with cloud services. Experts will be able to examine code used to stand up recipe foundations, explore new services, and gain additional perspectives. If the plethora of cloud services and combinations seem overwhelming to you, then this book is for you. The recipes in this book aim to provide “Hello, World” proofs of concept and components of enterprise-grade applications. This will be accomplished using common use cases with guided walk-throughs of scenarios that you can directly apply to your current or future work. These curated and experience-building recipes are meant to demystify services and will immediately deliver value, regardless of your AWS experience level.

# What You Will Learn

In addition to opening up new career opportunities, being able to harness the power of AWS will give you the ability to create powerful systems and applications that solve many interesting and demanding problems in our world today. Would you like to handle 60,000 cyber threats per second using AWS machine learning like [Siemens](https://oreil.ly/Qpyvy) does? Or reduce your organization’s on-premises footprint and expand its use of microservices like [Capital One](https://oreil.ly/vI0ZY) has? If so, the practical examples in this book will help expedite your learning by providing tangible examples showing how you can put the building blocks of AWS together to form practical solutions that address common scenarios. The on-demand consumption model, vast capacity, advanced capabilities, and global footprint of the cloud create new possibilities that need to be explored.

# The Recipes

We break the book into chapters that focus on general areas of technology (e.g., security, networking, artificial intelligence, etc.). The recipes contained within the chapters are bite-sized, self-contained, and easily consumable. Recipes vary in length and complexity. Each recipe has a problem statement, solution (with diagram), and discussion. Problem statements are tightly defined to avoid confusion. Solutions contain required preparation and steps to walk you through the work needed to accomplish the goal. When appropriate, explicit validation checks will be provided. We’ve also added extra challenges to the recipes to help you advance your learning if you wish to do so. Finally, we end each recipe with a short discussion to help you understand the solution and why it matters, suggestions to extend the solution, and ways to utilize it for real impact.

###### Note

To keep your AWS bill low and keep your account tidy, each recipe has cleanup steps provided in the repositories associated with the book.

Each chapter has its own repository at [_https://github.com/awscookbook_](https://github.com/awscookbook). The repository contains preparation steps for easy copying and pasting, required files, and infrastructure as code. We have also created GitHub templates for reporting bugs and suggesting new recipes. We encourage you to leverage GitHub to submit issues, create requests for new recipes, and submit your own pull requests. We will actively maintain the chapter repositories with updates for recipe steps and code in the README files of each recipe. Be sure to check these for any new or alternative approaches. We look forward to interacting with you on GitHub with new fun challenges and hints to assist you.

Some recipes are “built from scratch,” and others include preparation steps to allow you to interact with common scenarios seen in the real world. We have provided code to enable you to easily deploy the prerequisites. For example, [Recipe 6.5](https://learning.oreilly.com/library/view/aws-cookbook/9781492092599/ch06.html#updating_containers_with_bluesolidusgre), assumes that you are a container developer creating an application deployment that requires an existing network stack. When prerequisites exist, they can be “pre-baked” with preparation steps using code provided in the repositories. When substantial preparation for a recipe is needed, you will use the AWS Cloud Development Kit (CDK), which is a fantastic tool for intelligently defining and declaring infrastructure. The majority of the recipes are CLI based; when appropriate, we use console walk-throughs including screenshots or descriptive text.

###### Note

There are many ways to achieve similar outcomes on AWS; this book will not be an exhaustive list. Many factors will dictate the best overall solution for your use case. We have selected recipe topics to help you learn about AWS and make the best choices for your specific needs.

You’ll find recipes for things like the following:

  * Redacting personally identifiable information (PII) from text by using Amazon Comprehend

  * Automating password rotation for Amazon Relational Database Service (RDS) databases

  * Using VPC Reachability Analyzer to verify and troubleshoot network paths

Along with the recipes, we also provide short lines of code in the [Appendix](https://learning.oreilly.com/library/view/aws-cookbook/9781492092599/app01.html#fast_fixes) that will quickly accomplish valuable and routine tasks. We feel that these are great tidbits to add to your cloud toolbox.

###### Warning

AWS has a [free tier](https://aws.amazon.com/free), but implementing recipes in this book could incur costs. We provide cleanup instructions, but you are responsible for any costs in your account. We recommend checking out the [Well-Architected Labs](https://www.wellarchitectedlabs.com/) developed by AWS on expenditure awareness and leveraging [AWS Budgets actions](https://oreil.ly/4OVCc) to control costs.

# What You Will Need

Here are the requirements to get started and some tips on where to find assistance:

  * AWS account

    * [Setup instructions](https://oreil.ly/opuXX)

    * An IAM user with console and programmatic access

    * Administrator privileges for your IAM user

  * Personal computer/laptop

  * Software

    * Web browser (e.g., Microsoft Edge, Google Chrome, or Mozilla Firefox)

    * Terminal with bash or Z shell (Zsh)

    * Git

      * [Install instructions](https://github.com/git-guides/install-git)

    * Homebrew (optional but recommended to install other requirements)

      * [Install instructions](https://docs.brew.sh/Installation)

    * Code editor (e.g., VSCodium or AWS Cloud9)

      * Recommended install: `brew install --cask vscodium`

    * AWS CLI version 2 (2.1.26 or later)

      * [Install guide](https://oreil.ly/uYhyX)

      * Recommended install: `brew install awscli@2`

    * Python 3.7.9 (and pip) or later

      * Example install: `brew install python@3.7`

    * AWS Cloud Development Kit version 2.0 or later

      * [Getting started guide](https://oreil.ly/OmDu1)

      * Recommended install: `brew install npm` and `npm i -g aws-cdk@next`

  * Recommended: Create a folder in your home directory called _AWSCookbook_. This will allow you to clone each chapter’s repository in one place:
        
        AWSCookbook:$ tree -L 1
        .
        ├── AccountManagement
        ├── ArtificialIntelligence
        ├── BigData
        ...

###### Note

At the time of publishing, the AWS CDK has two versions: version 1 and version 2 (developer preview). The code we have provided is written for version 2. You can find out more information about how to migrate to and install CDK version 2 in this AWS [CDK v2 article](https://oreil.ly/jNyXH).

# Getting Started

This section provides examples of techniques and approaches we perform throughout the book to make the recipe steps easier to follow. You can skip over these topics if you feel comfortable with them. You can always come back and reference this section.

## Setups

In addition to the installation of the prerequisites listed previously, you will need the following access.

### AWS account setup

You will need a user with administrative permissions. Some of the recipes require the ability to create AWS Identity and Access Management (IAM) resources. You can follow the AWS guide for [creating your first IAM admin user and user group](https://oreil.ly/moVjA).

### General workstation setup steps for CLI recipes

We have created a group of code repositories available at [_https://github.com/awscookbook_](https://github.com/awscookbook). Create a folder called _AWSCookbook_ in your home directory (or any place of your choosing) and `cd` there:
    
    
    mkdir ~/AWSCookbook && cd ~/AWSCookbook

This will give you a place to check out chapter repositories (e.g., _Security_):
    
    
    git clone https://github.com/AWSCookbook/Security

Set and export your default Region in your terminal:
    
    
    export AWS_REGION=us-east-1

###### Tip

AWS offers many Regions across the world for cloud deployments. We’ll be using the us-east-1 Region for simplicity. As long as the services are available, there is no reason these recipes won’t work in other Regions. AWS has a list of [Regions and services](https://oreil.ly/I3eVB).

Set your AWS `ACCOUNT_ID` by parsing output from the `aws sts get-caller-identity` operation:
    
    
    AWS_ACCOUNT_ID=$(aws sts get-caller-identity \
         --query Account --output text)

###### Note

The `aws sts get-caller-identity` operation “[returns details about the IAM user or role](https://oreil.ly/XJMDp) whose credentials are used to call the operation.”

Validate AWS Command Line Interface (AWS CLI) setup and access:
    
    
    aws ec2 describe-instances

If you don’t have any EC2 instances deployed, you should see output similar to the following:
    
    
    {
      "Reservations": []
    }

###### Note

AWS CLI version 2 will by default send command output with multiple lines to `less` in your terminal. You can type **`q`** to exit. If you want to override this behavior, you can modify your _~/.aws/config_ file to [remove this default functionality](https://oreil.ly/SU9gk).

###### Tip

[AWS CloudShell](https://aws.amazon.com/cloudshell) is a browser-based terminal that you can use to quickly create a terminal environment in your authenticated AWS Console session to run AWS CLI commands from. By default, it uses the identity of your browser session to interact with the AWS APIs. Many of the recipes can be run using CloudShell. You can use CloudShell to run recipe steps, clean up commands, and other AWS CLI commands as your authenticated user, if you do not want to create a session that you use in your own local terminal environment on your workstation.

## Techniques and Approaches Used in This Book

The next few sections will explain and give examples of some ways of using the CLI to help you with recipes.

### Querying outputs, environment variables, and command substitution

Sometimes when subsequent commands depend on outputs from the command you are currently running. The AWS CLI provides the ability for [client-side filtering of output](https://oreil.ly/oV3cx). At times, we will set [environment variables](https://oreil.ly/39qp6) that contain these outputs by leveraging [command substitution](https://oreil.ly/FG9yl).

We’ll combine these three techniques to make things easier for you as you proceed through steps in the book. Here is an example:

Use the AWS Security Token Service (AWS STS) to retrieve your IAM user (or role) Amazon Resource Name (ARN) with the AWS CLI:
    
    
    aws sts get-caller-identity

You should see output similar to the following:
    
    
    {
      "UserId": "EXAMPLE",
      "Account": "111111111111",
      "Arn": "arn:aws:iam::111111111111:user/UserName"
    }

An example of querying for the ARN value and outputting it to the terminal follows:
    
    
    aws sts get-caller-identity --query Arn --output text

You should see output similar to the following:
    
    
    arn:aws:iam::111111111111:user/UserName

Query for the ARN value and set it as an environment variable using command substitution:
    
    
    PRINCIPAL_ARN=$(aws sts get-caller-identity --query Arn --output text)

To check the value of an environment variable, for example, you can `echo` it to the terminal:
    
    
    echo $PRINCIPAL_ARN

You should see output similar to the following:
    
    
    arn:aws:iam::111111111111:user/UserName

###### Tip

Using the `--dry-run` flag is always a good idea when performing an operation that makes changes—for example, `aws ec2 create-vpc --dry-run --cidr-block 10.10.0.0/16`.

### Replacing values in provided template files

Where possible, to simplify the learning experience for you, we have provided template files in the chapter code repositories that you can use as a starting point as input to some of the commands you will run in recipe steps. For example, when you create an AWS CodeDeploy configuration in [Recipe 6.5](https://learning.oreilly.com/library/view/aws-cookbook/9781492092599/ch06.html#updating_containers_with_bluesolidusgre), we provide _codedeploy-template.json_ with _`AWS_ACCOUNT_ID`_ , _`PROD_LISTENER_ARN`_ , and _`TEST_LISTENER_ARN`_ placeholders in the JSON file. We expect you to replace these placeholder values and save the file as _codedeploy.json_.

To further simplify your experience, if you follow the steps exactly and save these to environment variables, you can use the `sed` command to replace the values. Where possible, we provide you a command to do this, such as this example from [Chapter 6](https://learning.oreilly.com/library/view/aws-cookbook/9781492092599/ch06.html#containers):

Use the `sed` command to replace the values with the environment variables you exported with the _helper.py_ script:
    
    
    sed -e "s/AWS_ACCOUNT_ID/${AWS_ACCOUNT_ID}/g" \
         -e "s|PROD_LISTENER_ARN|${PROD_LISTENER_ARN}|g" \
         -e "s|TEST_LISTENER_ARN|${TEST_LISTENER_ARN}|g" \
         codedeploy-template.json > codedeploy.json

### Passwords

During some of the steps in the recipes, you will create passwords and temporarily save them as environment variables to use in subsequent steps. Make sure you unset the environment variables by following the cleanup steps when you complete the recipe. We use this approach for simplicity of understanding. A more secure method (such as the method in [Recipe 1.8](https://learning.oreilly.com/library/view/aws-cookbook/9781492092599/ch01.html#storingcomma_encryptingcomma_and_access)) should be used in production environments by leveraging AWS Secrets Manager.

#### Generation

You can use AWS Secrets Manager via the AWS CLI to [generate passwords](https://oreil.ly/7TxP4) with specific requirements. An example from [Chapter 4](https://learning.oreilly.com/library/view/aws-cookbook/9781492092599/ch04.html#databases) looks like this:
    
    
    ADMIN_PASSWORD=$(aws secretsmanager get-random-password \
         --exclude-punctuation \
         --password-length 41 --require-each-included-type \
         --output text \
         --query RandomPassword)

#### Usage and storage

In production environments, you should use [AWS Secrets Manager](https://oreil.ly/PUyzf) or [AWS Systems Manager Parameter Store](https://oreil.ly/HDMgB) (using secure strings) with IAM policies to control who and what can access the secrets. For simplicity, some of the policies of passwords and secrets used in the recipes might not be as locked down from a policy perspective as you would want in a production environment. Be sure to always write your own IAM policies to control this behavior in practice.

### Random suffixes

We generate a lot of random suffixes when we deal with global services like Amazon S3. These are needed because S3 bucket names need to be globally unique across the entire AWS customer base. Secrets Manager can be used via the CLI to generate a string that satisfies the naming convention and adds this random element to ensure all book readers can create resources and follow along using the same commands:
    
    
    RANDOM_STRING=$(aws secretsmanager get-random-password \
         --exclude-punctuation --exclude-uppercase \
         --password-length 6 --require-each-included-type \
         --output text \
         --query RandomPassword)

You can also use any other utilities to generate random strings. Some local tools may be preferred.

### AWS Cloud Development Kit and helper.py

A good place to start is the [“Getting started with the AWS CDK” guide](https://oreil.ly/OmDu1). After you have CDK 2.0 installed, if this is the first time you are using the AWS CDK, you’ll need to bootstrap with the Region you are working on with the AWS CDK toolkit:
    
    
    cdk bootstrap aws://$AWS_ACCOUNT_ID/$AWS_REGION

We use the AWS CDK when needed throughout the book to give you the ability to deploy a consistent scenario that aligns with the problem statement you see in the recipe. You can also choose to execute the recipe steps in your own existing environments, as long as you have the input variables required for the recipe steps. If things don’t work in your environment, you can stand up the provided environment and compare.

The CDK code we included in the repositories deploys resources using the AWS CloudFormation service, and we wrote output variables that you use in recipe steps. We created a Python script called _helper.py_ which you can run in your terminal to take the CloudFormation output and set local variables to make the recipe steps easier to follow—in most cases, even copy and paste.

An example set of commands for deploying CDK code for a recipe after checking out the chapter repository for [Chapter 4](https://learning.oreilly.com/library/view/aws-cookbook/9781492092599/ch04.html#databases), looks like the following:
    
    
    cd 401-Creating-an-Aurora-Serverless-DB/cdk-AWS-Cookbook-401/
    test -d .venv || python3 -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip setuptools wheel
    pip install -r requirements.txt
    cdk deploy

You can easily copy and paste the preceding code from the root of the chapter repository (assuming you have Python, pip, and CDK installed as prerequisites) to deploy the scenario that the solution will address in the solution steps of the recipe.

The _helper.py_ tool we created can then be run in your terminal after the `cdk deploy` is complete:
    
    
    python helper.py

You should see output that you can copy and paste into your terminal to set environment variables from the CDK CloudFormation stack outputs:
    
    
    $ python helper.py
    Copy and paste the commands below into your terminal
    ROLE_NAME='cdk-aws-cookbook-108-InstanceSS1PK7LB631QYEF'
    INSTANCE_ID='_random string here_ '

###### Note

Finally, a reminder that although we work for AWS, the opinions expressed in this book are our own.

Put on your apron, and let’s get cooking with AWS!

# Conventions Used in This Book

The following typographical conventions are used in this book:

_Italic_
    

Indicates new terms, URLs, email addresses, filenames, and file extensions.

`Constant width`
    

Used for program listings, as well as within paragraphs to refer to program elements such as variable or function names, databases, data types, environment variables, statements, and keywords.

**`Constant width bold`**
    

Shows commands or other text that should be typed literally by the user.

_`Constant width italic`_
    

Shows text that should be replaced with user-supplied values or by values determined by context.

###### Tip

This element signifies a tip or suggestion.

###### Note

This element signifies a general note.

###### Warning

This element indicates a warning or caution.

# Using Code Examples

Supplemental material (code examples, exercises, etc.) is available for download at [_https://github.com/awscookbook_](https://github.com/awscookbook).

If you have a technical question or a problem using the code examples, please send email to [_bookquestions@oreilly.com_](mailto:bookquestions@oreilly.com).

This book is here to help you get your job done. In general, if example code is offered with this book, you may use it in your programs and documentation. You do not need to contact us for permission unless you’re reproducing a significant portion of the code. For example, writing a program that uses several chunks of code from this book does not require permission. Selling or distributing examples from O’Reilly books does require permission. Answering a question by citing this book and quoting example code does not require permission. Incorporating a significant amount of example code from this book into your product’s documentation does require permission.

We appreciate, but generally do not require, attribution. An attribution usually includes the title, author, publisher, and ISBN. For example: “ _AWS Cookbook_ by John Culkin and Mike Zazon (O’Reilly). Copyright 2022 Culkins Coffee Shop LLC and Mike Zazon, 978-1-492-09260-5.”

If you feel your use of code examples falls outside fair use or the permission given above, feel free to contact us at [_permissions@oreilly.com_](mailto:permissions@oreilly.com).

# O’Reilly Online Learning

###### Note

For more than 40 years, [_O’Reilly Media_](http://oreilly.com/) has provided technology and business training, knowledge, and insight to help companies succeed.

Our unique network of experts and innovators share their knowledge and expertise through books, articles, and our online learning platform. O’Reilly’s online learning platform gives you on-demand access to live training courses, in-depth learning paths, interactive coding environments, and a vast collection of text and video from O’Reilly and 200+ other publishers. For more information, visit [_http://oreilly.com_](http://oreilly.com/).

# How to Contact Us

Please address comments and questions concerning this book to the publisher:

  * O’Reilly Media, Inc.
  * 1005 Gravenstein Highway North
  * Sebastopol, CA 95472
  * 800-998-9938 (in the United States or Canada)
  * 707-829-0515 (international or local)
  * 707-829-0104 (fax)

We have a web page for this book, where we list errata, examples, and any additional information. You can access this page at [_https://oreil.ly/AWS-cookbook_](https://oreil.ly/AWS-cookbook).

Email [_bookquestions@oreilly.com_](mailto:bookquestions@oreilly.com) to comment or ask technical questions about this book.

For news and information about our books and courses, visit [_http://oreilly.com_](http://oreilly.com/).

Find us on Facebook: [_http://facebook.com/oreilly_](http://facebook.com/oreilly)

Follow us on Twitter: [_http://twitter.com/oreillymedia_](http://twitter.com/oreillymedia)

Watch us on YouTube: [_http://youtube.com/oreillymedia_](http://youtube.com/oreillymedia)

# Acknowledgments

Thank you to Jeff Armstrong, author of _Migrating to AWS, A Manager’s Guide_ for introducing us to O’Reilly.

We want to recognize the tech reviewers who helped get this book to where it is today. Their keen eyes, opinions, and technical prowess are greatly appreciated. Jess Males, Gaurav Raje, Jeff Barr, Paul Bayer, Neil Stewart, David Kheyman, Justin Domingus, Justin Garrison, Julian Pittas, Mark Wilkins, and Virginia Chu—thank you.

Thanks to the knowledgeable community at [r/aws](https://www.reddit.com/r/aws) for always providing great insights and opinions.

Thank you to our production editor, Christopher Faucher, for getting the book in tip-top shape for release. Thanks also to our editor, Virginia Wilson, for taking the time to work with first-time authors during a pandemic. Your patience, suggestions, and guidance allowed us to complete this book and remain (somewhat) sane :-)