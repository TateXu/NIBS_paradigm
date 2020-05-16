

N_PAGES=24
for k in $(seq 1 ${N_PAGES}); do
    PAGES+=(A2_left_word.pdf);
    PAGES+=($k);
    PAGES+=(A2_right_word.pdf);
    PAGES+=($k);
done
pdfjoin ${PAGES[@]} --outfile A2_word.pdf