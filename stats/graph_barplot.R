
R version 3.0.0 (2013-04-03) -- "Masked Marvel"
Copyright (C) 2013 The R Foundation for Statistical Computing
Platform: x86_64-apple-darwin10.8.0 (64-bit)

R is free software and comes with ABSOLUTELY NO WARRANTY.
You are welcome to redistribute it under certain conditions.
Type 'license()' or 'licence()' for distribution details.

  Natural language support but running in an English locale

R is a collaborative project with many contributors.
Type 'contributors()' for more information and
'citation()' on how to cite R or R packages in publications.

Type 'demo()' for some demos, 'help()' for on-line help, or
'help.start()' for an HTML browser interface to help.
Type 'q()' to quit R.

[R.app GUI 1.60 (6476) x86_64-apple-darwin10.8.0]

[History restored from /Users/mquezada/.Rapp.history]

> setwd('~/Tesis/stats/data/')
> data = read.table('word_freqs_boston_total0.txt')
> par(las=2)
> barplot(data[2:100, 2], horiz=FALSE, names.arg=data[2:100, 1], cex.names= 0.6)