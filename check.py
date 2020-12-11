$ bash 1_get_urls.sh # has already been run
$ find ../raw_data -name "urls_*.txt" -exec sh -c "echo Number of URLs in {}: ; cat {} | wc -l" \;
Number of URLs in ../raw_data/drawings/urls_drawings.txt:
   25732
Number of URLs in ../raw_data/hentai/urls_hentai.txt:
   45228
Number of URLs in ../raw_data/neutral/urls_neutral.txt:
   20960
Number of URLs in ../raw_data/sexy/urls_sexy.txt:
   19554
Number of URLs in ../raw_data/porn/urls_porn.txt:
  116521
$ bash 2_download_from_urls.sh
$ bash 3_optional_download_drawings.sh # optional
$ bash 4_optional_download_neutral.sh # optional
$ bash 5_create_train.sh
$ bash 6_create_test.sh
$ cd ../data
$ ls train
drawings hentai neutral porn sexy
$ ls test
drawings hentai neutral porn sexy
