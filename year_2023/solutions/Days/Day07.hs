{-# LANGUAGE QuasiQuotes #-}

module Days.Day07
  ( day07,
  )
where

import AOC (Solution (..))
import Data.Char (digitToInt, isDigit)
import Data.List
import Data.List.Split
import Data.Ord
import Data.String.QQ
import Data.Text.Internal.Encoding.Utf16 (chr2)
import Debug.Trace
import Text.ParserCombinators.ReadP (get)

day07 :: Solution
day07 = Solution input' parseInput part1 part2

parseInput :: String -> [(String, Int)]
parseInput s = map (\l -> (head $ x l, read . head . tail $ x l)) (lines s)
  where
    x = splitOn " "

part1 :: [(String, Int)] -> Maybe Int
part1 xs =
  Just $ foldr ((+) . (\(i, (_, bet)) -> i * bet)) 0 $ zip [1 ..] $ trace ((unlines $ map fst $ (sortBy cardOrder xs))) $ sortBy cardOrder xs

cardOrder :: (String, Int) -> (String, Int) -> Ordering
cardOrder c1 c2 = case compare c1' c2' of
  EQ -> strongerCard (fst c1) (fst c2)
  LT -> LT
  GT -> GT
  where
    c1' = cardType $ fst c1
    c2' = cardType $ fst c2

strongerCard :: String -> String -> Ordering
strongerCard c1 c2 = compare c1' c2'
  where
    c1' = convertToNumbers c1
    c2' = convertToNumbers c2

convertToNumbers :: String -> [Int]
convertToNumbers [] = []
convertToNumbers (c : cs)
  | isDigit c = digitToInt c : convertToNumbers cs
  | c == 'T' = 10 : convertToNumbers cs
  | c == 'J' = 11 : convertToNumbers cs
  | c == 'Q' = 12 : convertToNumbers cs
  | c == 'K' = 13 : convertToNumbers cs
  | c == 'A' = 14 : convertToNumbers cs

cardType :: String -> Int
cardType cs =
  case cardOccourances cs of
    (5 : _) -> 7
    (4 : _) -> 6
    (3 : 3 : 3 : 2 : _) -> 5
    (3 : _) -> 4
    (2 : 2 : _) -> 3
    (2 : _) -> 2
    _ -> 1

cardOccourances :: String -> [Int]
cardOccourances cs = sortBy (comparing Data.Ord.Down) $ map (\c -> length (filter (== c) cs)) cs

part2 :: [(String, Int)] -> Maybe Int
part2 a = Just 1

input :: String
input =
  [s|
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
22662 1
AA5AA 743
AAKAA 246
AAAAQ 20
JJJJJ 171
|]

input' :: String
input' =
  [s|
K8KK6 75
TAK97 148
8345K 129
QT45K 170
77J7J 573
7JJK7 796
JQA74 769
3T733 204
KK66K 166
47222 657
56JTQ 527
2375J 424
36A63 352
JJKK3 513
373Q3 547
TT344 993
8A788 302
A7AAJ 625
646J4 270
J448Q 635
A7K7K 982
9QA96 876
77772 696
6K77Q 516
KJ33J 816
A292J 33
97Q77 488
KKK4K 856
AAQA7 511
365A4 784
252K2 144
J88JJ 389
25KKT 754
4T44T 951
975J9 357
K7637 799
3333K 942
2A4JT 929
5J595 750
77388 65
6K398 830
Q3K6J 605
333T3 537
44447 48
T958Q 624
48424 328
A9TQ7 793
T8558 838
47884 387
77AAA 890
J569Q 610
89T95 232
3A633 992
22JJA 651
J4639 367
4376K 957
593Q2 165
J2277 502
A3AAJ 451
68T9K 548
AAAQT 231
KK77Q 350
556J5 791
Q462K 421
T4J44 611
54T48 518
8K8AT 960
Q2Q82 258
AA7Q7 724
TTJAT 969
TT889 269
QA24Q 90
KK727 601
9Q745 41
8AA88 783
J4852 491
42454 425
327A4 145
98K87 604
A26T7 12
98Q8T 348
443QK 467
27478 10
K75KK 566
KKAQA 986
T5J35 371
78452 575
2398Q 426
83J63 428
83J65 471
6229T 866
9K333 108
9A2A9 564
7767J 306
3A849 822
2A7K7 979
QQQ7Q 230
2J2QJ 81
32JT3 833
KJK8K 127
73764 126
AA4JA 72
83363 365
99K9K 130
8KK8K 976
77JK8 981
JTAAA 164
JAQ36 113
5K5K5 183
J3222 508
444T4 654
TKKKK 965
A4A54 391
TT8T2 753
58J77 669
84356 340
TK7K4 868
KJ53T 941
A28J2 372
Q9995 961
AA55K 175
7779J 327
3JA6A 546
5JTAA 857
67768 558
KJ386 539
K632A 50
T2TTJ 119
A8TAQ 520
T3K58 795
K44J4 901
887T7 120
4J362 314
TKJ3K 423
44544 153
3Q23Q 369
A85AA 602
29993 44
QT4TQ 689
99A99 182
989J8 190
45454 962
46846 659
74877 915
A5636 603
65T5J 568
3J76T 203
2JQQQ 704
TJ856 254
6665K 220
6J38T 408
KKKKQ 222
6A55A 155
43337 888
33AA9 341
Q7QQK 719
979A7 275
9QTAQ 361
KTA73 448
A43QQ 878
2Q6J7 305
9T745 137
35Q58 596
QK4T3 85
78Q32 798
T29J6 606
QKQ6A 22
T2T5J 107
3JJK6 849
9JTTT 895
55855 676
49A65 407
27T72 899
4TTT9 201
77798 249
27222 773
5642J 834
95589 819
6JJ4K 485
4TJ56 437
96296 359
4444J 588
83777 663
J8555 757
KJKKK 524
43437 216
TJ6JT 154
7J787 894
36KKJ 288
J44J9 56
54KT2 921
QQ9J9 928
48AT6 854
AT7Q6 726
TTJJT 483
TKAKT 366
92938 615
7777J 210
TJ66T 752
7TA77 64
85693 478
KK232 242
88484 435
JA573 529
T9A65 886
35Q7T 25
8KK86 54
33343 841
QA346 185
6JQ66 809
AJQ78 217
557K7 290
QQQ29 450
K558K 409
6J722 832
44494 931
22729 789
32K97 671
22992 697
T9Q37 744
8J8J8 550
3367T 125
AJ725 255
QQA94 262
A446A 496
77678 650
J39Q5 110
89A8T 218
66Q6Q 701
J72KK 162
T2333 53
64382 179
54K27 777
A5T23 630
Q48QQ 644
22J2A 115
92735 620
99QQ7 686
33335 181
J42JJ 392
T6427 19
29T93 788
6Q72Q 474
A2AAA 40
4A2A6 595
QJ44Q 169
4453J 336
777Q5 619
2TTTT 97
7TQ95 687
22Q22 705
6QQ9A 551
2997Q 945
TTJ9J 466
49J52 785
26557 839
88497 691
TQ263 700
5JA5A 440
5A9KQ 202
JJT8T 685
2AA6A 599
JKK5T 292
3333A 200
2T6K7 920
9K4T7 460
74547 95
88538 297
77J73 36
53999 977
97988 376
94352 540
98888 598
KQAQQ 887
AKAA8 80
6J556 629
TA26A 195
55595 343
6T7K7 123
7JT84 268
K9828 879
J8K6K 543
23823 640
KK7QJ 380
AAAK4 926
7JTK4 388
AAKAA 246
77578 913
534AT 855
4K5K8 582
TA65T 172
AAQAK 514
86666 337
TQTJT 739
7477J 42
56TA8 585
2QK2Q 587
K938A 867
49449 319
55255 647
9AAAA 623
K4KK5 974
KQJ7Q 781
6T985 487
553A3 439
AA5AJ 987
QJ333 874
TJJJT 211
AJ9J7 464
9TK48 433
JJ6J6 192
TT44T 664
799AA 196
A8A94 782
7Q777 732
Q3Q99 88
T3A65 661
22442 881
72277 234
3KJ36 225
J3336 597
8JTJK 903
QQ43Q 277
Q5TKJ 583
AQTAQ 955
68888 892
TAT5A 557
44772 827
38338 442
96669 312
766J7 412
TK89T 713
33233 591
A99K9 150
44Q33 289
Q5585 52
5T3KK 161
J8J4T 51
7KK8K 475
2QAJ5 943
TTQ6Q 703
4Q56T 375
834K9 173
TTT5Q 354
272JA 975
J54Q5 490
6QK26 949
947KK 642
4AAA4 463
K796Q 678
QQA93 168
7JJ39 311
57779 504
K6JKJ 925
55775 158
4JA45 535
Q8323 560
A5J74 940
QQQ6J 160
6A3J4 953
A5256 469
6TTTA 677
Q3366 865
5T55T 427
3QQ3Q 414
AAQ9K 265
T6535 74
5892A 845
KK775 980
A738Q 446
6K5AQ 924
K5359 214
TQ968 614
87A97 507
4A4T3 988
QQAQ2 280
44934 385
QTJAJ 422
AA2A2 186
QKA94 444
8TK42 565
J2JA6 751
K2TAK 227
2Q5T7 626
23722 178
4Q2QQ 968
Q2Q42 432
77774 695
9KKJ9 330
ATJ49 935
T3682 828
57757 213
66949 572
495JA 294
K5KJ5 682
33K3A 198
462Q2 766
KQJKK 55
AQA98 207
88887 43
KK84K 104
8K8KA 958
QJ9QQ 73
4K444 641
5JK5A 149
7J99K 756
AT799 737
QJ2Q3 413
392J2 871
22JJ9 984
TTTAA 167
AJ2AA 643
82QK6 538
78877 774
93JQ8 103
92522 578
54446 429
36A87 381
2Q573 916
2323A 510
4AK85 228
266J2 76
49KT2 49
Q324J 346
J3843 708
T9399 78
53QQ5 592
99922 329
93669 35
43344 667
96J22 638
33633 394
6666Q 717
J2242 825
T879K 91
A8A22 253
26QQ2 47
83732 62
22K5J 553
T6628 379
J333J 322
6KK8T 709
2Q6J2 944
22J2T 417
QQK4Q 679
T993T 762
3666T 634
J43T2 850
A96KQ 9
88KK8 377
T67JK 967
AKQQJ 660
K222T 767
AAAQQ 272
47474 237
JJ999 403
J6666 247
TT7TJ 373
2A932 284
88837 954
5Q555 880
Q888Q 456
528A2 570
44642 273
262Q6 283
75595 806
58443 368
4464A 208
3833T 462
AAAAQ 20
K6873 370
3879A 824
73J26 718
72JJ5 776
AA9A9 652
K6646 184
36J66 68
28T88 790
5QJ55 238
2A2A2 221
J22J2 742
3JK89 668
9TT29 656
8K256 522
J8666 805
8869J 966
6K333 345
6A99A 728
TTA32 259
66776 2
44K64 187
AAAJJ 143
TT22T 684
955K5 71
TT2J2 729
78J94 287
88568 665
372JT 594
33J88 454
K3257 910
J5K3K 45
T6TT6 105
24972 586
85J84 461
4TJ45 618
3957Q 846
K2572 995
K4J8K 864
KKKK3 362
488Q4 758
64JKK 476
Q2Q7J 18
2856J 152
T994T 552
JA45A 404
4444A 436
7JA2T 477
J58JT 628
73J28 948
Q8T42 863
49977 922
J444J 205
T2769 420
7JT38 13
A8AAA 59
9JA92 58
7A77A 690
67686 655
8TJJA 731
AAAQ9 252
QQJ24 794
T99T6 525
49994 991
99669 98
KT54K 633
QAQQA 889
94TQ8 382
62266 27
5J999 248
Q3333 353
2A2AQ 159
TA759 733
53544 325
37Q6A 188
KK4J4 111
44Q73 323
4K67A 157
7K7K7 313
JKKJK 736
33573 764
3333J 484
3TTJ3 5
2QK6J 304
5Q37K 637
KQ476 66
56688 60
2KTAQ 612
K4J99 534
A4A73 1000
A5A55 533
3TQ36 31
TJQQT 317
9AJQT 674
77797 946
QJ827 554
69K99 443
5847A 410
7888J 692
Q5J58 219
77357 83
55QJ3 706
4347K 23
99A9A 308
9T73K 82
8Q456 517
5QQQQ 215
6T22T 763
7A82K 459
J5588 770
9J9JT 333
889A8 235
9AK74 131
A52J8 486
7AJJ7 418
J5A2J 902
36633 932
34543 985
55355 923
88478 296
88666 761
6266K 616
595Q8 989
A52KA 458
44467 748
2T7T7 627
TT25T 765
36725 191
KQKKT 840
88828 1
666JJ 493
TT58K 481
KKTKJ 37
J9333 282
3677J 39
84Q94 393
J8JJJ 658
3QJQJ 740
9378Q 549
56KK6 338
6J363 542
AJKKA 310
8J8KK 792
QKA5J 699
44646 808
TA6K7 430
76677 263
9Q987 498
A69J9 96
K3J2K 898
4A7T8 468
77494 693
JATA8 233
42K64 180
QJQ62 128
JK2KK 990
A7AAA 900
QK874 860
J4KK5 532
Q842Q 844
48JA2 978
65565 662
AJT8Q 114
KAJKK 206
22J22 46
93999 452
6677K 500
55378 6
2342J 891
3KKKJ 132
J9999 802
37373 622
5J459 482
AK648 177
Q52K6 226
AAJ64 318
999T9 561
48JK3 722
67265 730
8KQQK 872
QA579 398
522KK 16
55522 680
55765 324
835T7 315
6359K 38
K2QQ8 787
TTT86 734
777A7 576
6T866 136
K43Q6 479
58588 271
23323 29
JKAK2 14
A6936 499
9T92K 905
ATT28 851
J64K9 503
2TAK5 963
74875 138
3T553 670
755J7 384
5KK5Q 351
TT4TT 842
K6K22 501
2K222 807
8Q62J 526
36K2K 295
9TTKT 580
ATT9J 495
882Q9 786
22Q25 146
Q3TJ9 632
453TT 399
2A92A 303
A2J6A 813
55235 34
KTTJJ 326
2282T 286
9Q63T 811
8333A 688
J4554 241
K7K33 821
38427 646
T9956 556
49J94 100
3K887 363
35T7A 109
A722A 541
5A525 441
2T252 639
5QAJ7 117
A44Q4 122
8297J 473
32A4K 63
3A5JA 530
2AJA7 147
KAATK 710
AAQJQ 494
64968 212
A4J58 332
64944 397
ATQ68 3
43TTJ 301
95559 7
33393 101
55Q8Q 917
6QQQQ 698
AT59A 199
9AQ89 457
7J744 267
888J8 300
KJ888 581
AA557 257
T9TTT 893
45458 804
JQ529 694
J8AA9 636
KQJTK 820
T8A88 997
A25A2 912
676QJ 707
QQ7AQ 224
595A9 959
778J8 28
6562A 465
4K99T 908
Q5Q56 715
67K77 749
T2AJQ 316
7QQKK 140
739AQ 720
325J8 209
TTKKK 135
T8688 877
7KKKJ 334
42444 291
QQQT9 298
95999 347
22225 193
4J9JQ 15
J66QT 106
9TT2T 716
888Q8 559
9JJ8T 276
Q5Q5Q 4
79997 245
335AJ 711
8867J 673
476K8 907
J4343 431
822J6 8
JQ5Q5 562
89999 492
JTK2J 607
J46AT 102
A6AA8 569
J6J7J 768
92949 885
9Q4J7 972
K9499 406
69A83 589
J8K8J 914
K7A5K 87
54277 937
523JJ 383
J7295 139
QQQQT 142
78JA7 455
Q86T7 521
Q3393 747
44J49 279
7682A 897
T2322 250
44484 447
87435 800
A863A 30
6QT8T 489
AAKAK 320
8Q272 608
9676T 240
QQQJT 801
QQ77Q 189
TTTT3 344
J339Q 17
87878 621
7QTJQ 84
TA663 141
55554 236
88696 256
K22AT 331
9586K 579
3A453 21
76A85 176
5AJTJ 449
T4T7Q 349
54AA5 810
7JQ8T 947
99333 378
7QQ33 24
26622 681
T3KT5 480
8A8JQ 299
KJ9QQ 401
JAQ39 858
847AA 818
8QQJ2 952
A333A 400
4J489 307
4JKKJ 515
62222 771
94787 94
J955J 950
QJQ3T 577
TA3A3 197
Q8T39 121
TAAAA 600
2KJJJ 812
22822 613
J6888 260
65667 536
A75AK 741
997Q7 712
9QA44 497
A27KA 194
776JQ 339
577T7 402
33342 930
J4A53 918
3A3AA 453
2QQ22 772
TJTT3 11
K2KKK 938
6TTQ6 281
39923 735
4Q44Q 843
Q5Q55 321
T3T5A 434
QQQ7J 852
T974Q 574
777K8 545
46466 853
4KA53 584
T3Q3J 396
QJJQQ 509
5Q9J7 266
39QQQ 803
22242 69
25545 416
JJ555 649
77337 666
4T5K7 831
52K4J 567
555A5 57
45335 261
44644 124
JJJJJ 171
J9J64 355
66466 229
K4268 356
Q33Q3 725
TKTTT 999
86A86 869
33JKK 973
T69TT 904
T64K3 823
7T7TT 780
7Q478 760
6T625 738
KKKK9 309
8AQ75 983
QT39Q 92
KK82K 555
22J27 727
84948 156
89T67 927
T8AAK 133
Q3A72 778
Q2822 883
5J552 411
9K9A6 505
999J6 358
62A5A 118
Q6464 826
AJ666 934
Q8KKK 223
AT3J8 964
J7A96 829
3AK5K 861
68TQ3 360
T8Q88 919
AA24A 544
TJTTT 264
82686 415
45J9J 93
58Q7T 79
6Q665 251
55556 631
TTT43 239
J9595 746
AJAAA 648
98899 779
74AJA 675
89398 419
JQA5T 590
95K3J 70
A4AAA 836
A7J7A 61
33TQ4 243
Q9983 759
34K5Q 26
TJ77T 723
Q3937 174
A3259 609
KA24J 528
K56T3 151
459KT 342
66566 797
23A84 32
JJ383 896
9J222 405
6J764 862
44K4K 293
87Q94 67
7A923 815
5J58J 814
9487A 870
QKQQQ 438
396JT 519
44ATA 374
TK77J 395
A29AA 445
A2ATA 998
J9292 390
979Q9 939
5A2QT 683
977J9 653
TJA3Q 112
7J689 817
QQ677 859
J3J63 873
Q28Q3 994
A55JJ 523
K7462 364
65596 470
9Q45J 956
ATT2T 506
TK4QQ 875
AA5AA 743
28693 714
2J786 745
89T77 512
94474 884
3Q626 86
J742K 837
636KK 278
TA4TT 571
JQQQQ 563
8283Q 996
Q42K3 77
TTTT6 911
JTJ3J 835
555J5 847
J779K 244
35775 909
TQQ99 134
8A8Q8 163
36325 335
A9886 386
25T37 971
24A86 882
A9KAK 936
KQ7Q3 531
69666 89
39369 672
4J666 755
252Q5 775
2TJA8 933
56566 645
7QA92 593
3KKQK 617
AQ896 906
99992 721
JTQ9J 848
K5KKK 970
43TAA 702
KQ97A 472
24A44 274
TK2J7 116
K6666 99
48845 285
|]
