#!/usr/bin/env bash

set -Eeuo pipefail

if [[ -z "${TELEGRAM_BOT_TOKEN:-}" ]]; then
  echo "Error: TELEGRAM_BOT_TOKEN is not configured."
  exit 1
fi

if [[ -z "${TELEGRAM_CHAT_ID:-}" ]]; then
  echo "Error: TELEGRAM_CHAT_ID is not configured."
  exit 1
fi

MESSAGE="${1:-Good morning! This is your daily GitHub Actions notification.}"

echo "Sending Telegram message..."

response="$(
  curl \
    --silent \
    --show-error \
    --fail-with-body \
    --request POST \
    "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage" \
    --data-urlencode "chat_id=${TELEGRAM_CHAT_ID}" \
    --data-urlencode "text=${MESSAGE}"
)"

echo "${response}"
echo "Telegram message sent successfully."