

N_PAGES=87
for k in $(seq 1 ${N_PAGES}); do
    PAGES+=(B1_left_word.pdf);
    PAGES+=($k);
    PAGES+=(B1_right_word.pdf);
    PAGES+=($k);
done
pdfjoin ${PAGES[@]} --outfile A2_word.pdf