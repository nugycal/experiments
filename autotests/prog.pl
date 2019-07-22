#!/usr/bin/env perl
my @words;
foreach my $arg (@ARGV) {
    my $count = 0;
    my $new = $arg;
    $new =~ tr/A-Z/a-z/;
    foreach my $letter (split(//, $new)) {
        if ($letter eq "a" or $letter eq "e" or $letter eq "i" or $letter eq "o" or $letter eq "u") {
            $count++;
        }
        elsif ($count < 3) {
            $count = 0;
        }
    }
    if ($count ge 3) {
        push @words, $arg;
    }
}

my $str = join " ", @words;
print "$str\n";
