CREATE TABLE `property_likes` (
  `id` INT AUTO_INCREMENT PRIMARY KEY
    COMMENT 'Unique identifier for each like record',
  
  `property_id` INT NOT NULL
    COMMENT 'Reference to the property that has been liked',
  
  `user_id` INT NOT NULL
    COMMENT 'Reference to the user who has liked the property',
  
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    COMMENT 'Timestamp indicating when the like was made',
  
  FOREIGN KEY (`property_id`) REFERENCES `property`(`id`) ON DELETE CASCADE
    COMMENT 'Foreign key constraint linking to the property table; deletes like if property is deleted',
  
  FOREIGN KEY (`user_id`) REFERENCES `users`(`id`) ON DELETE CASCADE
    COMMENT 'Foreign key constraint linking to the users table; deletes like if user is deleted',
  
  UNIQUE KEY `unique_property_user` (`property_id`, `user_id`)
    COMMENT 'Unique constraint to ensure a user can only like a property once'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;