# SurveyPal (Developed during the NASA OLS Nebula 2024.1 Pilot Cohort)

A streamlined Telegram bot powered by AI to simplify and accelerate the process of creating, conducting and analysing research surveys.

## Features

Here are some key features I am working to implement in SurveyPal bot:

- Streamlined survey creation
- Generate survey questions with AI
- AI-powered survey reporting & analysis
- Real-time survey responses and statistics
- Conduct surveys with SurveyPal in telegram groups
- Multi-language support

Your `contribution` will be most welcomed

BETA: [SurveyPal](https://t.me/surveypal_bot)

<hr>

- [Bot structure](#bot-structure)
- [Getting started](#getting-started)
  _ [First steps](#first-steps)
  _ [Configure environment variables](#configure-environment-variables)
  _ [Bot settings](#bot-settings)
  _ [Database](#database)
  - [Docker](#docker)
  _ [Start bot](#start-bot)
  _ [Manage bot container](#manage-bot-container)
  _ [View bot logs](#view-bot-logs)
  _ [Restart bot](#restart-bot)
  _ [Stop bot](#stop-bot)
  _ [Database postgres](#database-postgres)
  _ [Manage postgres via psql](#manage-postgres-via-psql)
  _ [Migrations](#migrations)
  _ [Create revision](#create-revision)
  _ [Upgrade database](#upgrade-database)
  _ [I18n locales](#i18n-locales)
  _ [Create locales](#create-locales) \* [Update locales](#update-locales)
  <hr>

## Bot structure

````bash
├───bin                 # bash scripts for docker
├───bot
│   ├───filters         # aiogram filters
│   ├───handlers
│   │   ├───errors      # error handlers
│   │   ├───tasks       # tasks handlers
│   │   └───users       # message handlers
│   ├───keyboards
│   │   ├───default     # aiogram markups
│   │   └───inline      # aiogram inline markups
│   ├───middlewares     # aiogram middlewares
│   └───states          # aiogram states
├───data
│   ├───locales         # i18n locales
│   └───logs            # bot logs
├───models              # database models
├───services            # database services
└───utils               # utilities

## Getting started

To get started with SurveyPal, follow these steps:

### First steps

1. Clone the repository:

    ```bash
    git clone https://github.com/iamdLite/SurveyPal.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Configure environment variables

#### Bot settings

1. Create a `.env` file in the root directory of the project.

2. Add the following environment variables to the `.env` file:

    ```plaintext
    BOT_TOKEN=your-bot-token
    ```

    Replace `your-bot-token` with the token of your Telegram bot.

#### Database

1. Install PostgreSQL if you haven't already.

2. Create a new PostgreSQL database.

3. Add the following environment variables to the `.env` file:

    ```plaintext
    DB_HOST=your-db-host
    DB_PORT=your-db-port
    DB_NAME=your-db-name
    DB_USER=your-db-username
    DB_PASSWORD=your-db-password
    ```

    Replace `your-db-host`, `your-db-port`, `your-db-name`, `your-db-username`, and `your-db-password` with the appropriate values for your database.

### Docker

To run SurveyPal using Docker, follow these steps:

#### Start bot

1. Build the Docker image:

    ```bash
    docker build -t surveypal .
    ```

2. Run the Docker container:

    ```bash
    docker run -d --name surveypal surveypal
    ```

#### Manage bot container

To manage the SurveyPal Docker container, use the following commands:

- View container logs:

  ```bash
  docker logs surveypal
````

- Restart container:

  ```bash
  docker restart surveypal
  ```

- Stop container:

  ```bash
  docker stop surveypal
  ```

#### Database postgres

To manage the PostgreSQL database, follow these steps:

##### Manage postgres via psql

1. Connect to the PostgreSQL database:

   ```bash
   psql -h your-db-host -p your-db-port -U your-db-username -d your-db-name
   ```

   Replace `your-db-host`, `your-db-port`, `your-db-username`, and `your-db-name` with the appropriate values for your database.

2. Execute SQL queries or commands.

##### Migrations

To create and upgrade the database migrations, follow these steps:

###### Create revision

1. Generate a new migration revision:

   ```bash
   alembic revision --autogenerate -m "Your migration message"
   ```

   Replace `"Your migration message"` with a descriptive message for your migration.

###### Upgrade database

1. Apply the database migrations:

   ```bash
   alembic upgrade head
   ```

### I18n locales

To manage the internationalization (i18n) locales, follow these steps:

#### Create locales

1. Create a new locale file in the `data/locales` directory.

2. Add the translations for the locale.

#### Update locales

1. Update the existing locale files in the `data/locales` directory with the updated translations.
