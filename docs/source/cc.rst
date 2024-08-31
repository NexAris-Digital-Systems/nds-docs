Introduction
==============
Welcome to the Control Center Discord bot documentation. Here you will find information about the bot, its features, and commands to help you get the most out of it.

``tip``
=======

.. tip::

   Got new command ideas?

   Come by and drop them in our discord server - https://crazydev.org/discord


.. list-table:: Commands
   :widths: 25 25 25 25
   :header-rows: 1

   * - Command Name
     - Description
     - Options
     - [Coming Soon] Required Permissions

   * - /announce
     - Send an announcement via the bot.	
     - [channel] [message]
     - Manage Messages Permission

   * - /auto-react
     - Send an announcement via the bot.	
     - [emoji] [channel]
     - N/A (Will be fixed in the next update)

   * - /avatar
     - 	View a user's avatar.
     - [user]
     - N/A

   * - /bot-info	
     - Displays information about the bot.
     - N/A
     - N/A

   * - /bot-info	
     - Displays information about the bot.
     - N/A
     - N/A

   * - /cat
     - 	Sends a random image of a cat.
     - N/A
     - N/A

   * - /channel crate 
     - 	Create a discord  channel
     - [name] [type] [category]
     - Manage Channels

   * - /channel delete 
     - 	Delete a discord  channel
     - [channel] [reason]
     - Manage Channels

   * - /channel lock 
     - 	Lock  a discord  channel
     - [channel]
     - N/A (Will be fixed in the next update)

   * - /channel unlock 
     - 	Unlock  a discord  channel
     - [channel]
     - N/A (Will be fixed in the next update)

   * - /dadjoke 
     - Sends a random dadjoke
     - N/A
     - N/A 

   * - /invites
     - 	View how many members a user has invited to a server
     - [user]
     - N/A 

   * - /logging-channels 
     -  Enable logging for your server.
     - [channel]
     - N/A (Will be fixed in the next update)

   * - /members 
     - 	View how many users have a specified role.	
     - [role]
     - N/A 

   * - /nick 
     - 	Change a user's nickname in a Discord server.	
     - 	[target] [new_nick]
     - Manage Nicknames Permission

   * - /poll-create 
     - 	Creates a poll.	
     - [option1] [option2] [option3]
     - N/A (Will be restricted to administrators in the future update to prevent abuse or any related issues)

   * - /members 
     - 	View how many users have a specified role.	
     - [role]
     - N/A 

   * - /quote 
     - 	Sends an inspirational quote.	
     - N?A
     - N/A 

   * - /rate 
     - Rate a user from 1-10
     - [user]
     - N/A 

   * - /reminder
     - Sets a reminder for the specified amount of time
     - [time] [messaeg]
     - N/A

   * - /report
     - Found a user abuse our services? Report them to Crazydev Moderation ASAP!
     - [user] [reason] [proof] 
     - 

   * - /role add
     - Adds the specified role to a user
     - [user] [role]
     - Manage Roles

   * - /role remove
     - Removes the specified role to a user
     - [user] [role]
     - Manage Roles

   * - /role all
     - Adds the specified role to everyone on the server.
     - [role] [include_bots]
     - Manage Roles

   * - /role create 
     - Create a new role.
     - [name] [color] [hoist]
     - N/A (Will be fixed in the next update)

   * - /role delete 
     - Delete a new role.
     - [name] [color] [hoist]
     - N/A (Will be fixed in the next update)

   * - /role remove
     - Removes a role from a user
     - [user] [role]
     - N/A (Will be fixed in the next update)

   * - /roles
     - Lists all server roles
     - N/A
     - N/A 

   * - /rtd
     - Roll a dice or flip a coin.	
     - [arg]
     - N/A

   * - /say
     - Send a message as the bot
     - [message] [embeded]	
     - N/A (Will be restricted to server admins soon)

   * - /server avatar
     - View the server's avatar
     - N/A
     - N/A

   * - /server banner
     - View the current server's banner
     - N/A
     - N/A

   * - /server info   
     - View information about current server
     - N/A
     - N/A

   * - /server invite
     - Sends current server invite link. (If there are none, one will be created)
     - N/A
     - N/A

   * - /slowmode
     - Set slowmode for a discord text channel
     - [channel] [time]
     - Manage Messages

   * - /softban 
     - Softban a member from current server. (Deletes messages from past 7 days)
     - 	[user] [reason]
     - Ban Members permission

   * - /stats
     - View the current statistics of the bot.	
     - N/A
     - N/A

   * - /status-page
     - Sends a link to our Status page.
     - N/A
     - N/A

   * - /support
     - Sends a link to our support server.
     - N/A
     - N/A

   * - /trivia
     - Sends a trivia question.	
     - N/A
     - N/A

   * - /vc deafen
     - Deafen a member from a voice channel.
     - [member] [reason] [dm]
     - Deafen Members Permission

   * - /vc disconnect
     - Disconnects a member from a voice channel.
     - [member] [reason] [dm]	
     - Deafen Members Permission

   * - /vc mute
     - Mute a user from a voice channel.
     - [member] [reason] [dm]
     - Mute Members Permission

   * - /vc unmute
     - Unmute a user from a voice channel.
     - [member] [reason] [dm]	
     - Mute Members Permission

   * - /vc undeaf
     - Undeaf a member from a voice channel.	
     - [member]	
     - N/A (Will be fixed in the next update)

   * - /voidcase
     - Remove a warning from a user.
     - [user] [case_number]
     - Kick Members Permission 

   * - /warnings
     - View a user's warnings for current server.
     - [user]
     - Kick Members Permission

   * - /weather
     - View the weather for the specified city
     - [city]
     - N/A

   * - /whois
     - Displays information about the specified user.
     - [user]
     - N/A

   * - /help
     - Sends a basic help message.
     - N/A
     - N/A

   * - /ban
     - Ban a user from the current server
     - [user] [reason]
     - Ban Members Permission

   * - /kick 
     - Kicks a specified user from current server
     - [user] [reason]
     - Kick Members Permission

   * - /unmute	
     - Unmute a user in the server. ("Untimeout")
     - [user]
     - Moderate Members (Will be fixed in a future update)

   * - /warn
     - Issues a warning to a user.	
     - [user] [reason]
     - Kick Members permission

   * - /purge
     - Deletes a specified number of messages from current channel.	
     - [number]
     - Manage Messages Permissions

   * - /prefix
     - Change the bot's prefix [Server Only]
     - [number]
     - Manage Messages Permissions
