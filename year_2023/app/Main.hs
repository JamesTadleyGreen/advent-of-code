module Main where

import Criterion.Main
import Days.Day01
import Days.Day02
import Days.Day03

main :: IO ()
main = defaultMain [bench "test" $ nfIO (print day03)]
