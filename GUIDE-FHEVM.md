# Sécurité FHEVM

## Flux confidentiel

Suivre la donnée depuis le chiffrement côté client jusqu’à son utilisation on-chain et son éventuel déchiffrement. Distinguer ciphertext, handles, métadonnées et résultat public.

## Autorisations

Examiner les ACL, les contrats autorisés à manipuler un handle, les délégations et les conditions de déchiffrement. Une fuite d’autorisation peut annuler la confidentialité sans casser le chiffrement.

## Intégrité

La confidentialité ne prouve ni la validité de l’entrée ni la correction du calcul. Documenter les contrôles métier, les permissions d’appel et la correspondance entre résultat demandé et résultat rendu.

## Limites

Préciser le schéma, le bruit, les coûts, les parties de confiance et les informations révélées par le contexte. Ne pas présenter FHEVM comme une garantie universelle de confidentialité.
