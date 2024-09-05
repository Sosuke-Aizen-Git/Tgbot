Telegram Bot ProjectOverviewThis repository contains a Telegram bot that provides various functionalities including link generation, user management, and more. The bot is built using Python and utilizes the Pyrogram library for interacting with the Telegram API.Features/start: Initializes the bot and greets users./genlink: Generates a unique link based on user-provided messages./batch: Handles batch operations for link generation./add_admin: Adds a new admin to manage the bot./remove_admin: Removes an existing admin./users: Shows the total number of users who started the bot./ping: Displays the bot’s uptime./force_join_channel1: Sets a channel as required for users to join./force_join_channel2: Sets a second channel as required for users to join./remove_force_join1: Removes the first force join channel requirement./remove_force_join2: Removes the second force join channel requirement./fatch_anime: Fetches anime-related information from specified channels.InstallationClone the Repository:git clone https://github.com/yourusername/telegram-bot.git
cd telegram-botInstall Dependencies:Ensure you have Python installed.Create a virtual environment (optional but recommended):python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`Install the required Python packages:pip install -r requirements.txtConfigure Environment Variables:Create a .env file in the root directory and add your environment variables:BOT_TOKEN=your_bot_token
MONGO_URL=your_mongodb_urlUsageRun the Bot:python bot.pyInteracting with the Bot:Start the bot by sending /start in a private chat.Use other commands as listed in the Features section.Configurationconfig.py: Contains configuration settings including the bot token and MongoDB URL.helper_func.py: Contains utility functions used by the bot.ContributingFork the repository and create a new branch.Make your changes and create a pull request.Ensure your code adheres to the project’s coding standards.LicenseThis project is licensed under the MIT License - see the LICENSE file for details.ContactDeveloper: Your NameEmail: your.email@example.com
