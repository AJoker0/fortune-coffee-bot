# Fortune Coffee Bot

Welcome to **Fortune Coffee Bot** — your personal assistant for choosing drinks and getting random daily tasks. This bot helps you pick your coffee, snack, or drink based on your mood and also shares random positive phrases and tasks for the day!

## What the bot can do:
- **Pick a drink**: The bot gives you options like latte, matcha, frappe, and more.
- **Daily task**: It sends you a helpful task to start your day on a positive note.
- **Fortune cookie**: Choose a drink, and the bot gives you a "fortune" or motivational phrase.
- **Always online**: Thanks to the **UptimeRobot** service, the bot stays active and doesn’t go to sleep on free Render plans.

## How to run it:

1. Clone the repo:
   ```bash
   git clone https://github.com/AJoker0/fortune-coffee-bot.git
   cd fortune-coffee-bot
   
2. Install dependencies:

pip install -r requirements.txt

3. Add a .env file in the root of the project and include your API_TOKEN for Telegram:

API_TOKEN=your_bot_token

4. Start the bot:

    python bot.py

5. For **Render and UptimeRobot ** or other platforms, use keep_alive.py to keep the bot online by periodically pinging it.

Project structure:

    bot.py: Main bot logic.

    keep_alive.py: Keeps the bot online and prevents it from going to sleep.

    predictions.py: List of positive phrases.

    keyboard.py: The drink selection keyboard.

    tasks.py: List of daily tasks.

    .env: File for secret stuff like your Telegram bot token.

Important:

    Never share your bot token publicly! Use environment variables (.env) to keep it safe.

    The bot uses Flask and aiogram to interact with users via Telegram.

License:

This project is licensed under MIT. Check [LICENSE]([url](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository#applying-a-license-to-a-repository-with-an-existing-license)) for more details.

Make sure to add .env to .gitignore so you don’t accidentally push your token to GitHub. Stay safe!

Thanks for using the bot! ☕💻


Now you can simply copy the content and use it as your **README.md** file. To add it to your repository:

1. Create the **README.md** file in the project’s root folder.
2. Paste the content above.
3. Commit and push the changes:
   ```bash
   git add README.md
   git commit -m "Add README"
   git push
