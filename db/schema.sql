CREATE TABLE IF NOT EXISTS `user` (
  `user_id` INTEGER PRIMARY KEY,
  `username` TEXT CHECK ( LENGTH(username) <= 255) UNIQUE NOT NULL,
  `password` TEXT NOT NULL,
  `registred_at` INTEGER,
  `role` TEXT CHECK( role in ('admin', 'moderator', 'author', 'viewer', 'blocked') ),
  FOREIGN KEY (role) REFERENCES `roles` (`role_name`)
);

CREATE TABLE IF NOT EXISTS `last_online_user` (
  `online_id` INTEGER PRIMARY KEY,
  `online_time` INTEGER,
  `user` INTEGER,
  FOREIGN KEY (user) REFERENCES `user` (`user_id`)
);

CREATE TABLE IF NOT EXISTS `user_tokens` (
  `user` INTEGER,
  `token` TEXT CHECK ( LENGTH(token) <= 255),
  `created` INTEGER,
  `valid_until` INTEGER,
  FOREIGN KEY (user) REFERENCES `user` (`user_id`)
);

CREATE TABLE IF NOT EXISTS `roles` (
  `role_name` TEXT CHECK( role_name in ('admin', 'moderator', 'author', 'viewer', 'blocked') ) PRIMARY KEY,
  FOREIGN KEY (role_name) REFERENCES `roles` (`role_name`)
);

CREATE TABLE IF NOT EXISTS `role_permission` (
  `role_name` TEXT CHECK ( LENGTH(role_name) <= 255),
  `write_comment` INTEGER CHECK ( write_comment IN (0,1) ),
  `edit_comments` INTEGER CHECK ( edit_comments IN (0,1) ),
  `remove_comments` INTEGER CHECK ( remove_comments IN (0,1) ),
  `write_posts` INTEGER CHECK ( write_posts IN (0,1) ),
  `edit_post` INTEGER CHECK ( edit_post IN (0,1) ),
  `remove_posts` INTEGER CHECK ( remove_posts IN (0,1) ),
  `add_user` INTEGER CHECK ( add_user IN (0,1) ),
  `view_user` INTEGER CHECK ( view_user IN (0,1) ),
  `remove_user` INTEGER CHECK ( remove_user IN (0,1) ),
  FOREIGN KEY (role_name) REFERENCES `user` (`user_id`)
);

CREATE TABLE IF NOT EXISTS `post` (
  `post_id` INTEGER PRIMARY KEY,
  `author_id` INTEGER,
  `publised_at` INTEGER,
  `edited_at` INTEGER,
  `article` text,
  `visebility`TEXT CHECK( visebility IN ('public', 'hidden', 'private') ),
  FOREIGN KEY (post_id) REFERENCES `post` (`post_id`)
);

CREATE TABLE IF NOT EXISTS `comments` (
  `comment_id` INTEGER PRIMARY KEY,
  `post_id` INTEGER,
  `comment_author` INTEGER,
  `commemts` text,
  `upvotes` INTEGER,
  FOREIGN KEY (comment_author) REFERENCES `user` (`user_id`)
);

CREATE TABLE IF NOT EXISTS `replyTo` (
  `thread_id` INTEGER PRIMARY KEY,
  `comment_id` INTEGER,
  FOREIGN KEY (comment_id) REFERENCES `comments` (`comment_id`) 
);