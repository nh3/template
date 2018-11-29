#!/usr/bin/env bats

# Test matrix2mtx

setup() {
    bats_script="$(basename $BATS_TEST_FILENAME)"
    exec="${bats_script::-5}"
    dir="${BATS_TEST_FILENAME::-5}"
    cmd="$exec $dir/input.txt $dir/test"

    expected_mtx="$dir/output.mtx"
    expected_genes="$dir/output_genes.tsv"
    expected_barcodes="$dir/output_barcodes.tsv"

    test_mtx="$dir/test.mtx"
    test_genes="$dir/test_genes.tsv"
    test_barcodes="$dir/test_barcodes.tsv"
}

teardown() {
    if [[ $status != 0 ]]; then
        echo "$cmd"
    fi
}

@test "run" {
    run $cmd
    [[ "$status" -eq 0 ]]
}

@test "mtx" {
    [[ $(diff -q "$expected_mtx" "$test_mtx") == "" ]]
}

@test "genes" {
    [[ $(diff -q "$expected_genes" "$test_genes") == "" ]]
}

@test "barcodes" {
    [[ $(diff -q "$expected_barcodes" "$test_barcodes") == "" ]]
}

