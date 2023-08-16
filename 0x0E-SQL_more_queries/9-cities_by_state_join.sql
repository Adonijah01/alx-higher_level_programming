-- Lists all cities in database hbtn_0d_usa.
-- records are being  sorted in order of ascending cities.id.
SELECT c.`id`, c.`name`, s.`name`
  FROM `cities` AS c
       INNER JOIN `states` AS s
       ON c.`state_id` = s.`id`
 ORDER BY c.`id`;
-- adonijah kiplimo.
