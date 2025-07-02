echo "Sample\tGroup" > metadata_with_counts.txt

for f in *_1P.fastq; do
  # Determine base name (e.g., SRR55789100) from _1P
  base=$(echo "$f" | sed 's/_1P.fastq//')

  # Determine group based on _1P file
  if echo "$f" | grep -q "man_1P.fastq$"; then
    group="control"
  else
    group="case"
  fi

  # Output for both files
  echo "${base}_1P.fastq\t${group}"
  echo "${base}_2P.fastq\t${group}"
done >> metadata_with_counts.txt


