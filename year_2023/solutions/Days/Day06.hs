{-# LANGUAGE QuasiQuotes #-}

module Days.Day06
  ( day06
  ) where

import AOC (Solution(..))
import Data.Char (isDigit)
import Data.List.Split
import Data.String.QQ
import Debug.Trace
import Text.ParserCombinators.ReadP (get)

day06 :: Solution
day06 = Solution input' parseInput part1 part2

parseInput :: String -> [[Int]]
parseInput s =
  map
    (map (read :: String -> Int) .
     filter (not . null) . splitOn " " . last . splitOn ":")
    (lines s)

part1 :: [[Int]] -> Maybe Int
part1 (times:distances:_) =
  Just $ calculateError times distances

calculateError :: [Int] -> [Int] -> Int
calculateError [] [] = 1
calculateError (t:ts) (d:ds) = numberOfWins t d * calculateError ts ds

numberOfWins :: Int -> Int -> Int
numberOfWins time distance =
  foldr
    (\t i ->
       if (time - t) * t > distance
         then i + 1
         else i)
    0
    [1 .. time - 1]

part2 :: [[Int]] -> Maybe Int
part2 a = part1 $ combineNumbers a


combineNumbers :: [[Int]] -> [[Int]]
combineNumbers xs = [[time], [distance]]
  where (time:distance:_) = map ((read :: String -> Int) . concatMap show) xs

input :: String
input =
  [s|
Time:      7  15   30
Distance:  9  40  200
|]

input' :: String
input' =
  [s|
Time:        44     80     65     72
Distance:   208   1581   1050   1102
|]
