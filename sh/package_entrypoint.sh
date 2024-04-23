cd /code
mkdir -p /test/.cache/pants/lmdb_store/immutable/files
chown -R root /test/.cache/pants/lmdb_store/immutable/files
curl --proto '=https' --tlsv1.2 -fsSL https://static.pantsbuild.org/setup/get-pants.sh | bash -s -- --bin-dir /usr/local/bin
/usr/local/bin/pants --no-watch-filesystem --no-pantsd --no-local-cache package ::