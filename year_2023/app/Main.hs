module Main where

import Criterion.Main
import Days.Day01
import Days.Day02
import Days.Day03
import Days.Day04

main :: IO ()
main = defaultMain [bench "test" $ nfIO (print day04)]
-- main = print day04
