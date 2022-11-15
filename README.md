- Run install-solana.sh
- Run the test validator daemon
   solana-test-validator &
- Build and deploy the oracle
   pushd oracle
   npm run build:program-rust
   solana program deploy dist/program/helloworld.so
   popd
- run the docker stack
   docker-compose up
- run the oracle client
   pushd oracle
   npm run start
   popd
