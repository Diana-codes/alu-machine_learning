-- 103-average_weighted_score.sql
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
  DECLARE avg_score FLOAT;

  SELECT 
    SUM(c.score * p.weight) / SUM(p.weight)
  INTO avg_score
  FROM corrections c
  JOIN projects p ON c.project_id = p.id
  WHERE c.user_id = user_id;

  UPDATE users
  SET average_score = avg_score
  WHERE id = user_id;
END //

DELIMITER ;
