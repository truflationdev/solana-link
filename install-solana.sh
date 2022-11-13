#!/bin/bash

#https://rustup.rs/
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

#https://docs.solana.com/cli/install-solana-cli-tools
sh -c "$(curl -sSfL https://release.solana.com/stable/install)"
