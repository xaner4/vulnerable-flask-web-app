insert into "user" ("user_id", "username", "password", "registered_at", "role")
values (1, "admin", "7d5b09e09b986f8792dbd4b947ce7e13", 1587980569, "admin"), (69, "John Doh", "6c9b8b27dea1ddb845f96aa2567c6754", "1600000000", "moderator");
-- admin:ThisIsMySecretPassword && John Doh:pa$$w0rd

insert into "post" ("author_id", "publised_at", "edited_at", "title", "article", "visebility")
values 
(1, 1587980687, 1587981687, "You seem malnourished. Are you suffering from intestinal parasites?", "This is the first article on this blog", "public"),
(69, 1487980687, 1499999687, "We can't compete with Mom! Her company is big and evil! Ours is small and neutral!", "Noooooo! Bender, I didn't know you liked cooking. That's so cute. WINDMILLS DO NOT WORK THAT WAY! GOOD NIGHT! Soon enough. WINDMILLS DO NOT WORK THAT WAY! GOOD NIGHT! I didn't ask for a completely reasonable excuse! I asked you to get busy! A true inspiration for the children.", "hidden"),
(1,1345676892, 1515930230, "You mean it controls your actions?", "Alderaan? I'm not going to Alderaan. I've got to go home. It's late, I'm in for it as it is. You are a part of the Rebel Alliance and a traitor! Take her away! I have traced the Rebel spies to her. Now she is my only link to finding their secret base.", "public"),
(69, 1598780687, 0, "Hey, Luke! May the Force be with you.", "But with the blast shield down, I can't even see! How am I supposed to fight? Don't act so surprised, Your Highness. You weren't on any mercy mission this time. Several transmissions were beamed to this ship by Rebel spies. I want to know what happened to the plans they sent you. Ye-ha! I call it luck. Dantooine. They're on Dantooine. The plans you refer to will soon be back in our hands.", "public");
