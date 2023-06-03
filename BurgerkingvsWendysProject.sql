-- Identifying the Datasets
SELECT *
FROM Burgerking

SELECT *
FROM Wendys


-- Looking to see which items have from most to least in calories

--Max
SELECT TOP 5 Item, Category, MAX(Calories) AS Calories
FROM Burgerking
GROUP BY Item, Category
ORDER BY Calories DESC;

SELECT TOP 5 Item, Category, Max(Calories) AS Calories
FROM Wendys
GROUP BY Item, Category
ORDER BY Calories DESC


--Min
SELECT TOP 5 Item, Category, MIN(Calories) AS Min_Calories
FROM Burgerking
GROUP BY Item, Category
ORDER BY Min_Calories ASC;

SELECT TOP 5 Item, Category, MIN(Calories) AS Min_Calories
FROM Wendys
GROUP BY Item, Category
ORDER BY Min_Calories ASC



-- Counting how many types of items for Burgerking
SELECT DISTINCT Category
FROM Burgerking

SELECT COUNT(Category) AS Burgers
FROM Burgerking
WHERE Category LIKE 'Burgers'

SELECT COUNT(Category) AS Chicken
FROM Burgerking
WHERE Category LIKE 'Chicken'

SELECT COUNT(Category) AS Fish
FROM Burgerking
WHERE Category LIKE 'Fish'

SELECT COUNT(Category) AS Breakfast
FROM Burgerking
WHERE Category LIKE 'Breakfast'

SELECT COUNT(Category) AS Sauces
FROM Burgerking
WHERE Category LIKE 'Sauce'


-- Counting how many types of items for Wendys
SELECT DISTINCT Category AS Total_Items
FROM Wendys

SELECT DISTINCT COUNT(Category) AS Total_Amount
FROM Wendys

SELECT COUNT(Category) AS Burgers
FROM Wendys
WHERE Category LIKE 'Burgers'

SELECT COUNT(Category) AS Chicken
FROM Wendys
WHERE Category LIKE 'Chicken'

SELECT COUNT(Category) AS Breakfast
FROM Wendys
WHERE Category LIKE 'Breakfast'


--Deleting unnecessary column to keep Data more tidy
ALTER TABLE Burgerking
DROP COLUMN Weight_Watchers

ALTER TABLE Wendys
DROP COLUMN Weight_Watchers

--Average/Balanced Item Choices
SELECT TOP 5 Item, Category, AVG(Calories) AS Balanced_Calories
FROM Burgerking
WHERE Category LIKE 'Breakfast'
GROUP BY Item, Category
ORDER BY Balanced_Calories

SELECT TOP 5 Item, Category, AVG(Calories) AS Balanced_Calories
FROM Burgerking
WHERE Category LIKE 'Burgers'
GROUP BY Item, Category
ORDER BY Balanced_Calories

SELECT Item, Category, AVG(Calories) AS Balanced_Calories
FROM Burgerking
WHERE Category LIKE 'Fish'
GROUP BY Item, Category
ORDER BY Balanced_Calories


--Joins/Unions between Burgerking and Wendys
SELECT *
FROM Burgerking AS Bk
INNER JOIN Wendys AS W
	ON Bk.Calories = W.Calories


SELECT *
FROM Burgerking AS Bk
LEFT JOIN Wendys AS W
	ON Bk.Calories = W.Calories

SELECT *
FROM Burgerking AS Bk
RIGHT JOIN Wendys AS W
	ON Bk.Calories = W.Calories

SELECT *
FROM Burgerking AS Bk
FULL OUTER JOIN Wendys AS W
	ON Bk.Calories = W.Calories


--Identifying the items with the most calories in descending order between Burgerking and Wendys
SELECT Item, Calories from Burgerking
UNION
Select Item, Calories from Wendys
ORDER BY Calories DESC

