{-# LANGUAGE GADTs #-}

module AOC
  ( Solution(..)
  ) where

import Data.Text (Text)

data Solution where
  Solution
    :: (Show b)
    => String
    -> (String -> a)
    -> (a -> Maybe b)
    -> (a -> Maybe b)
    -> Solution

instance Show Solution where
  show (Solution input parseInput part1 part2) =
    unlines
      [ "Part 1: " <> show (part1 (parseInput input))
      , "Part 2: " <> show (part2 (parseInput input))
      ]
