# UI スタイルガイド & 技術仕様書 — Rabiloo Webサイト デザイン規約

---

## 1. はじめに & デザイン方針（Design Direction）

本デザイン規約は **Professional & Modern Tech** の思想に基づいて構築されています。グローバルなテクノロジー企業が持つ正確さと信頼性を、デジタル時代・AI時代の革新性と躍動感と組み合わせたスタイルです。

### クリエイティブ方向性 & ムードボード（Vibe & Moodboard）
* **ブランドパーソナリティ（Brand Personality）**: プロフェッショナル、ミニマル、洗練、最新テクノロジー。第一印象から「信頼できる・鋭い」という感覚を与えることが目標です。
* **ムードボード**: テクノロジー・デジタルトランスフォーメーション・AIの現代的な精神を正確に伝える配色・レイアウト・動きを持つUI参考例を5〜10点収集します。
* **UIデザイン原則（UI Principles）**:
  - **明瞭性（Clarity）**: 明確なグリッドレイアウトと整然とした情報階層により、B2B顧客が技術力と事例（ケーススタディ）を直感的に理解できるようにします。
  - **革新のアクセント（Dynamic Accents）**: ミニマルなデジタル背景の上で、メインカラーをアクセントとして際立たせ、強力なCTA（行動喚起）を実現します。
  - **グローバルな体験（Global Feel）**: 現代的なサンセリフフォント、国際標準に合わせた余白、マルチデバイス（レスポンシブ：モバイル & デスクトップ）への最適化。

---

## 2. カラーシステム（Color Palette & Tokens）

カラーパレットはモダンさとテクノロジー志向の未来感を表現するように設計されています。メインカラーはダークネイビーブルー（Primary Blue）で、アクティブなオレンジ（Accent Orange）と、高い産業的審美性を保つダーク・グレー系の色調を組み合わせます。

### カラーロール（Color Roles）

#### ブランドカラー（Brand Colors）
* **Pure White（`#FFFFFF`）**: サイト全体のメイン背景色。ページの背景は常に `#FFFFFF` 固定とし、ミニマル・明るさ・最大の余白感を確保します。
* **Primary Blue / プライマリ（`#003BBA`）**: すべてのコンポーネントのメインカラー（メインCTAボタン・重要な見出し・アクティブ状態・メインナビゲーションなど）。
* **Accent Orange / アクセント（`#FF9900`）**: アクセントカラーのオレンジ。非常に節度を持って使用します（主に目立つステータスタグ・バッジ・視覚的なアクセントとなる小さなグラフィック要素）。大きなコンポーネントの背景色として乱用してはいけません。

#### サポート & ニュートラルカラー（Supporting & Neutral Colors）
背景・カードフレーム・区切り線・テキスト色に使用する明から暗へのニュートラルカラーパレット：
* **Text / Primary（`#111111`）**: 本文および大見出しのメインテキスト色。最高のコントラスト比を確保します。
* **Text / Secondary（`#565656`）**: 説明文や補足情報のサブテキスト色。
* **Text / Inactive / Muted（`#C0C0C0`）**: 無効（Disabled）状態のテキストやプレースホルダーのテキストに使用。
* **Border（`#D1D1D1`）**: 区切り線（Borders・Dividers）の色。空間を明確に分割します。
* **Bg / Tag（`#F6F6EE`）**: タグラベルの背景色。
* **Bg / Card Background（`#F8F7F5`）**: カードまたはパネルの背景色。

#### セマンティックカラー（Semantic Colors）
システムの状態を表す固定カラーコード：
* **Success（成功）**: グリーン。操作が正常に完了したことを表します。
* **Warning（警告）**: イエロー/オレンジ。操作実行前にユーザーに注意を促します。
* **Error（エラー）**: レッド。エラー通知または危険なアクションを表示します。
* **Info（情報）**: ブルー。有用なガイダンス情報を表示します。

> [!IMPORTANT]
> **オンカラールール（On-Color：背景に対応するテキスト色）:**
> コンテンツが常に読みやすいよう、規約では各背景色に対応するテキスト色を「On-[色名]」として定義します。例：Primary（`#003BBA`）の青い背景上のテキストは、必ずOn-Primary（例：白 `#FFFFFF`）を使用しなければなりません。

---

## 3. タイポグラフィシステム（Typography）

UIの一貫した表示とテクノロジー記事のSEO最適化を確保するため、フォントシステムはモダンなサンセリフ書体を採用し、Retinaディスプレイで鮮明に表示される高品質なシステムフォントを優先します。見出しと主要コンポーネントには **Neue Montreal**（現代的なテクノロジー感を演出）を使用し、サイト全体でフォントは最大2種類に抑えます。

### フォントアセット（Font Assets）
**SVN Neue Montreal** フォントセットはプロジェクト内にローカル保存され、Google Driveにもアップロードされています：
* **OpenTypeフォント（.otf）**: [OTF](./assets/Font%20ch%E1%BB%AF/OTF) · ☁️ [Driveからダウンロード](https://drive.google.com/drive/folders/1N7rnBGgzKIxm7K9xav4xOJYKi1YV7ZIN)（Webサイトとグラフィックデザイン両方に使用）
  * `SVN-NeueMontreal-Thin.otf` / `ThinItalic.otf`
  * `SVN-NeueMontreal-Light.otf` / `LightItalic.otf`
  * `SVN-NeueMontreal-Book.otf` / `BookItalic.otf`
  * `SVN-NeueMontreal-Regular.otf` / `Italic.otf`
  * `SVN-NeueMontreal-Medium.otf` / `MediumItalic.otf`
  * `SVN-NeueMontreal-SemiBold.otf` / `SemiBolditalic.otf`
  * `SVN-NeueMontreal-Bold.otf` / `BoldItalic.otf`

### タイポグラフィスケール & ウェイト規約（Typography Scale & Weights）

Figmaデザインとコーディング（CSS）の両方に対応するため、文字サイズと太さ（Font Weight）の階層は以下の**3段階**に統一して使用します：

- **H1**: **SemiBold（600）** を使用。
- **H2**: **Regular（400）** を使用。
- **その他すべてのテキスト**（本文・H3・ラベル・リンクなど）: **Medium（500）** を使用。

#### Figmaデザインスケール（デザインデータ上の値）
* **トップページ メイン見出し（H1）**: フォントサイズ: `96pt` / SemiBold 600 / 行間: `130%` / 字間: `-1%`
* **セクション見出し（H2）**: フォントサイズ: `56pt` / Regular 400 / 行間: `1.1` / 字間: `0%`
* **大型統計数字（Stat Number）**: フォントサイズ: `86pt` / Medium 500 / 行間: `90%`
* **カード見出し / サブ見出し（H3 / Sub-heading）**: フォントサイズ: `24pt` / Medium 500 / 行間: `1.3`
* **本文テキスト（Body）**: フォントサイズ: `18pt` / Medium 500 / 行間: `150%`
* **ボタンラベル / リンク（Label / Link）**: フォントサイズ: `16pt` / Medium 500 / 行間: `150%`

#### CSS/Dev実装スケール（コーディング実装用の値）
開発者はライブWebサイトに合わせた以下の標準サイズを使用します：
* **トップページ メイン見出し（H1）**: `96px` / SemiBold（600）/ 行間: `130%`（`1.3`）
* **セクション メイン見出し（H2）**: `56px` / Regular（400）/ 行間: `1.1`
* **大型統計数字（Stat Number）**: `86px` / Medium（500）/ 行間: `90%`（`0.9`）
* **サブ見出し / カード（H3 / Sub-heading）**: `24px` / Medium（500）/ 行間: `1.3`
* **本文テキスト（Body Text）**: `18px` / Medium（500）/ 行間: `150%`（`1.5`）
* **ボタン / リンク（Button Label / Footer Link）**: `16px` / Medium（500）/ 行間: `24px`（`1.5`）

---

## 4. レイアウト・グリッド & スペーシングシステム（Layout & Spacing Grid）

Webサイトはグリッド原則を厳密に遵守し、大型デスクトップ画面でのコンテンツ比率の最適化と、モバイルへの縮小時の滑らかなブロック折り畳みを実現します。

### グリッドシステム（Grid System）
* **デスクトップ（PC画面）**: 標準12カラムグリッドを使用。コンテンツ最大表示幅（Max-container width）は `1200px`〜`1440px` に固定。カラム間のガター（Gutter）は `24px` または `30px` で固定。
* **モバイル（600px以下のスマートフォン画面）**: 4カラムグリッドに変換（コンテンツ量に応じて1〜2カラムに）。画面端にコンテンツが触れないよう、両端のセーフエリアパディング（マージン）は最低 `16px` を確保します。

### スペーシング規則（Spacing Scale）
すべての間隔（padding・margin・gap）は8pxを基本倍数としたグリッドシステムで規格化されます（4pxは非常に小さな要素やタグにのみ使用）：
* **トークン xs（4px）/ sm（8px）**: アイコンとテキスト間の間隔、または小さなタグ内のパディングに使用。
* **トークン md（16px）/ lg（24px）**: 同一カードブロック内の小さな要素間の間隔（カードパディング・レイアウトギャップ・小見出しマージン）に使用。
* **トークン xl（32px）/ xxl（40px）/ xxxl（60px〜80px）**: トップページの大きなセクション間を区切る上下のマージンに使用。

### 角丸システム（Shape / Corner Radius）
統一された角丸レベルで調和のとれたUIを実現します：
* **Sharp（0px）**: 角丸なし。完全にフラットな枠線に使用。
* **Soft/Small（4px）**: テキスト入力フィールド・ツールチップ・メインアクションボタン（CTAボタン）に使用。
* **Medium（8px〜12px）**: 小さなカード・ドロップダウンメニューに使用。
* **Large（16px〜24px）**: 大きなダイアログボックス・大きな画像に使用。
* **Pill（9999px または 50%）**: 丸タグ・アバター・特殊なグラフィック要素を完全に丸くする場合に使用（ボタンには使用不可）。

### 重なり & シャドウシステム（Elevation & Shadows）
3D空間でのレイヤー重なり構造を表現します：
* **Flat**: 影なし。地面に接するフラットな要素に使用。
* **Elevated（Hover）**: マウスオーバー時にインタラクション可能な要素を示す非常に軽い影。
* **Overlay**: ユーザーの完全な注意を引くためにポップアップ・ダイアログの最上部に表示される、深みのあるソフトな影。

---

## 5. ビジュアルアセット規約（Visual Assets）

* **アイコノグラフィー（Iconography）**:
  ミニマルで均一な細線スタイルのアイコンライブラリ（**Untitled UI Icons**）を使用します。同一画面上で異なるアイコンスタイルを混在させることは絶対に禁止です。
  * **フォルダパス**: [assets/Untitled UI Icons](./assets/Untitled%20UI%20Icons) · ☁️ [Drive上のアイコン一式](https://drive.google.com/drive/folders/1mk_9yylXxZmqGLk9HpZoxdFDsIrzClR9)
  * **利用可能なカテゴリ**:
    - [Alert & Feedback](./assets/Untitled%20UI%20Icons/Alert%20%26%20Feedback) · ☁️ [Drive](https://drive.google.com/drive/folders/1SPgjA6C10Eo_cVvJOyKWtyskChmne14L): 警告・エラー・成功・ローディング状態。
    - [Arrows](./assets/Untitled%20UI%20Icons/Arrows) · ☁️ [Drive](https://drive.google.com/drive/folders/1F3_pGX7jP2eh4p2_zuk_Gy4W7xmZ_5A-): ナビゲーション矢印・スクロールボタン・ドロップダウン・アコーディオン。
    - [Charts](./assets/Untitled%20UI%20Icons/Charts) · ☁️ [Drive](https://drive.google.com/drive/folders/1NSog-eWvR-CbvktwEkJWlp9_q_ZsZLnr): 分析グラフ・データ統計。
    - [Communications](./assets/Untitled%20UI%20Icons/Communications) · ☁️ [Drive](https://drive.google.com/drive/folders/1twudxbD6tswcChMhp84MnNNQ3RysppnU): メッセージ・電話・メール・チャット・連絡。
    - [Development](./assets/Untitled%20UI%20Icons/Development) · ☁️ [Drive](https://drive.google.com/drive/folders/1a-7vmssRfVmj7dld4OlsbeekoWMOS9ER): 技術設定・プログラミング・API連携。
    - [Editor](./assets/Untitled%20UI%20Icons/Editor) · ☁️ [Drive](https://drive.google.com/drive/folders/1D8glHi8Jfy2hGcbf9zz2dNw1Y_STqKQP): 編集ツール・テキスト書式設定。
    - [Education](./assets/Untitled%20UI%20Icons/Education) · ☁️ [Drive](https://drive.google.com/drive/folders/1FY20xdwzy8X66EuTlFDjZkESI0Q4xGCG): 学習・資格・知識。
    - [Files](./assets/Untitled%20UI%20Icons/Files) · ☁️ [Drive](https://drive.google.com/drive/folders/1a2GFNirdk7G-Y_r6L5oGXx_YbanPYhV6): ファイル・ドキュメント管理・アップロード/ダウンロード。
    - [Finance & E-Commerces](./assets/Untitled%20UI%20Icons/Finance%20%26%20E-Commerces) · ☁️ [Drive](https://drive.google.com/drive/folders/1K-mQuhCyaV-E3ZsnBt4hDsaLAor378OK): 決済・カート・取引・銀行カード。
    - [General](./assets/Untitled%20UI%20Icons/General) · ☁️ [Drive](https://drive.google.com/drive/folders/1-iAnAm3DmDUprMEpUN5x5GWzIRqtH1vO): 共通の基本アイコン（設定・検索・ホーム・ゴミ箱など）。
    - [Images](./assets/Untitled%20UI%20Icons/Images) · ☁️ [Drive](https://drive.google.com/drive/folders/1aXvxD2otmaE5GWjqdUp-MBK3cS1qE7iw): カメラ・アルバム・画像フィルター。
    - [Layout](./assets/Untitled%20UI%20Icons/Layout) · ☁️ [Drive](https://drive.google.com/drive/folders/1RBUtM9M_UAgFqR9Dg-oxncYM9Sfd38Pq): ページレイアウト・カラム/行の分割。
    - [Map & Travel](./assets/Untitled%20UI%20Icons/Map%20%26%20Travel) · ☁️ [Drive](https://drive.google.com/drive/folders/1QHeKadcShzRfU0w-Bi9fjS3diGzsFGqW): 位置情報（マップピン）・地図・移動。
    - [Media & Devices](./assets/Untitled%20UI%20Icons/Media%20%26%20Devices) · ☁️ [Drive](https://drive.google.com/drive/folders/1ue-G3sJfllV2Oq7Y-QUmTxhmKtU85HlO): スマートフォン・PC・再生・停止・音量。
    - [Security](./assets/Untitled%20UI%20Icons/Security) · ☁️ [Drive](https://drive.google.com/drive/folders/1LvPi5jI6zBbGInx1Q0sUAsCrgnfZkY6o): ロック・セキュリティ・アカウント認証。
    - [Shapes](./assets/Untitled%20UI%20Icons/Shapes) · ☁️ [Drive](https://drive.google.com/drive/folders/1whqXzTsDrOGWpuuZZ0jisOdjweBYwgSP): 基本的なグラフィック図形。
    - [Time](./assets/Untitled%20UI%20Icons/Time) · ☁️ [Drive](https://drive.google.com/drive/folders/141MgIHMmLXSYkUZx2oNiKNj8hkU56Fxf): 時計・時間・カレンダー予約。
    - [Users](./assets/Untitled%20UI%20Icons/Users) · ☁️ [Drive](https://drive.google.com/drive/folders/1jn5xcIbRAlqOQNOsXhTyEhLK6aOPYmPg): ユーザーアカウント・プロフィール・グループ権限。
    - [Weathers](./assets/Untitled%20UI%20Icons/Weathers) · ☁️ [Drive](https://drive.google.com/drive/folders/1RSj7i86CeZKt7ULF_zi0-H5qd1f-lgWI): 天気・雲・雨・晴れ。

* **ロゴシステム（Logo Identity System）**:
  ブランドアイデンティティは2つの明確なロゴバージョンに分かれており、異なる表示スペースと目的に対応します。[assets/Logo](./assets/Logo) · ☁️ [Driveのロゴフォルダ](https://drive.google.com/drive/folders/1p9Xt6n2ghjh7LBiKviCmGqdNbbPCjXxQ) を参照してください：
  - **ロゴR（シンボル/ファビコン — Rの文字のみ）**:
    - *特徴*: 最大限にミニマル化したバージョン。スタイライズされた **R** の文字のみを残します。
    - *使用場面*: Webサイトのファビコン・SNSのプロフィールアバター・またはスペース節約のためにモバイル/サイドバーで折りたたんだ状態のロゴ（collapsed menu）として使用します。
    - ☁️ [DriveのロゴRフォルダ](https://drive.google.com/drive/folders/1P0kHKNQ9ivnzNtoLAN7HgVIiI4RZ-PFF)
    - *ファイル一覧*:
      - [Favicon xanh.svg](./assets/Logo/Logo%20R/Favicon%20xanh.svg): 明るい背景用のブランドブルー版。
      - [Favicon trắng -01.svg](./assets/Logo/Logo%20R/Favicon%20tr%E1%BA%AFng%20-01.svg): ダーク背景用の白い細線版。
      - [LOGO XANH 2023-07.svg](./assets/Logo/Logo%20R/LOGO%20XANH%202023-07.svg): シンボルの完全なベクター形式。
  - **フルロゴ（Full Logo）**:
    - *特徴*: Rシンボルとブランドロゴタイプがセットになった完全版。
    - *使用場面*: メインヘッダーバー（デスクトップ版）・フッターエリア・プレゼンテーションスライド・契約書類・公式マーケティング資料に使用します。
    - ☁️ [DriveのフルロゴフォルダDrive](https://drive.google.com/drive/folders/14vlHX92ZIjtDypA69-KP8vBsqC2DO9pO)
    - *ダーク/モノクロ版の優先ルール*:
      - **最優先**: ブランドのオレンジをアクセントとして残す必要がある黒白表示（またはダーク背景）には [LOGO 2023-06-03.png](./assets/Logo/Logo%20Full/LOGO%202023-06-03.png) を使用します。
      - **代替案**: ダーク背景またはオレンジを表示できない特殊な単色印刷の場合にのみ [LOGO trang-05.png](./assets/Logo/Logo%20Full/LOGO%20trang-05.png)（完全な白版）を使用します。
    - *ファイル一覧*:
      - [LOGO.png](./assets/Logo/Logo%20Full/LOGO.png): ブランドカラーの完全なオリジナル版。
      - [LOGO 2023-06-03.png](./assets/Logo/Logo%20Full/LOGO%202023-06-03.png): オレンジをアクセントとして残したモノクロ版（推奨）。
      - [LOGO trang-05.png](./assets/Logo/Logo%20Full/LOGO%20trang-05.png): 完全な白版（オレンジを表示できない場合のみ使用）。
      - [LOGO 2023-07-07-02.png](./assets/Logo/Logo%20Full/LOGO%202023-07-07-02.png): 2023年7月更新版。
      - [LOGO 2023-08-01.png](./assets/Logo/Logo%20Full/LOGO%202023-08-01.png): 2023年8月更新版。

* **フォトグラフィースタイル（Photography Style）**:
  - **実写写真**: スタッフや実際の職場環境の本物の写真を使用します。信頼スコア（Trust score）を高めるため、インターネット上のストック写真の使用は極力避けます。
  - **サービス説明用イラスト（AI・Eコマース）**: モダンなアイソメトリック（等角投影）ベクターグラフィック、またはクリーンなコントラストのデータモデルを使用し、テクノロジー感のあるグレー・ブルー系の配色にオレンジのアクセントを組み合わせます。

---

## 6. ランディングページ構成 & UIコンポーネント定義（Landing Page Anatomy）

ランディングページの唯一の目的は、企業顧客（B2B）にコンバージョンアクション（コンサルティング申込・ソリューションへのお問い合わせ）を実行させることです。UIコンポーネントは以下の構成に従う必要があります：

### 必須セクションの構成（Landing Page Sections）

---

#### 🔷 ヘッダー（Header — スティッキー固定）

**実装ファイル**: [`components/header-footer.html`](./components/header-footer.html)

##### 構成 & サイズ
| 属性 | 値 |
|---|---|
| 高さ | `72px` 固定 |
| 背景色 | `#FFFFFF` |
| 下ボーダー | `1.5px dashed #D1D1D1` |
| 位置 | `sticky`、`top: 0`、`z-index: 1000` |
| コンテンツ最大幅 | `1440px` |
| 左右パディング | `60px`（デスクトップ）・`32px`（タブレット）・`16px`（モバイル）|
| レイアウト | `flex`、`justify-content: space-between` — 左側ロゴ・右側ナビ |

##### ロゴ（左側）
- **ファイル**: [`LOGO.png`](./assets/Logo/Logo%20Full/LOGO.png) · ☁️ [Drive](https://drive.google.com/drive/folders/14vlHX92ZIjtDypA69-KP8vBsqC2DO9pO) — 白背景用のブランドカラーロゴ。
- **表示サイズ**: `height: 36px`、`width: auto`。

##### ナビゲーション（右側）
すべてのナビゲーション項目は共通のタイポグラフィを使用します：

| 属性 | 値 |
|---|---|
| フォントサイズ | `20px` |
| フォントウェイト | `400`（Regular）|
| 行間 | `1.3` |
| パディング | `8px` |
| デフォルトテキスト色 | `#111111` |
| ホバー時テキスト色 | `#003BBA` |
| トランジション | `0.18s ease` |

**項目の順序（左 → 右）**:

| # | 項目 | 種類 | 備考 |
|---|---|---|---|
| 1 | `[ AI Employee ]` | テキストリンク | 色 `#003BBA`、`[ ]` は実際のテキスト文字（ボーダーではない）|
| 2 | `会社概要` | ドロップダウン | 4項目: 成長の軌跡・技術力・ストーリー・ニュース |
| 3 | `サービス` | ドロップダウン | 5項目: AIサービス・AIコンサルティング・AIエージェント開発・AI統合・デジタルトランスフォーメーション |
| 4 | `導入事例` | リンク | ドロップダウンなし |
| 5 | `ナレッジ` | ドロップダウン | 3項目: ブログ・Eブック・ウェビナー |
| 6 | `採用` | リンク | ドロップダウンなし |
| 7 | `JA` | ドロップダウン | 言語切替: 🇻🇳 ベトナム語 · 🇬🇧 English · 🇯🇵 日本語 |

##### ドロップダウンメニュー
| 属性 | 値 |
|---|---|
| 背景 | `#FFFFFF` |
| ボーダー | `1px solid #D1D1D1` |
| 角丸 | `8px` |
| ボックスシャドウ | `0 16px 42px rgba(0,0,0,.12), 0 2px 8px rgba(0,0,0,.05)` |
| 最小幅 | `232px`（標準）・`416px`（メガメニュー）|
| パディング | `6px` |
| 表示アニメーション | `opacity 0→1` + `translateY(6px→0)`、`0.18s ease` |
| シェブロンアイコン | ホバー時に `180deg` 回転、`14×14px`、`stroke-width: 2` |

##### レスポンシブ — モバイル（≤ 1024px）
- デスクトップナビは非表示。`40×40px` のハンバーガーボタンを表示。
- 全画面オーバーレイ（`position: fixed`、`inset: 0`、`z-index: 1001`）、背景 `#FFFFFF`。
- オーバーレイパディング: `92px 33px 48px`。
- **モバイルナビのタイポグラフィ**: `font-size: 30px`、`font-weight: 500`、`line-height: 1.15`。
- サブメニューアコーディオン: `font-size: 19px`、`color: #565656`、`padding-left: 18px`。
- AI Employeeはテキスト `[ AI Employee ]` で色 `#003BBA` として表示。

---

#### 🔷 フッター（Footer）

**実装ファイル**: [`components/header-footer.html`](./components/header-footer.html)

##### 構成 & サイズ
| 属性 | 値 |
|---|---|
| 背景色 | `#010511` |
| 上パディング | `72px` |
| コンテンツ最大幅 | `1440px` |
| 左右パディング | `60px`（デスクトップ）・`32px`（タブレット）・`16px`（モバイル）|

##### フッターロゴ
- **ファイル**: [`LOGO 2023-06-03.png`](./assets/Logo/Logo%20Full/LOGO%202023-06-03.png) · ☁️ [Drive](https://drive.google.com/drive/folders/14vlHX92ZIjtDypA69-KP8vBsqC2DO9pO) — ダーク背景に適したオレンジアクセントを残したモノクロ版。
- **表示サイズ**: `height: 36px`、`width: auto`、`margin-bottom: 28px`。

##### 4カラムグリッド
| カラム | コンテンツ | 幅比率 |
|---|---|---|
| 1 — 企業情報 | ロゴ + 2オフィスの住所 | `2.4fr` |
| 2 — 会社概要 | ナビゲーションリンク 4件 | `1fr` |
| 3 — サービス | サービスリンク 5件 | `1fr` |
| 4 — ナレッジ | リンク 3件 | `1fr` |

**レスポンシブ**: `1fr 1fr`（≤ 1024px）・`1fr`（≤ 600px）。

##### タイポグラフィ — カラム見出し
| 属性 | 値 |
|---|---|
| フォントサイズ | `16px` |
| フォントウェイト | `600` |
| 行間 | `20px` |
| テキスト色 | `#FFFFFF` |
| 下パディング | `16px` |
| デコレーター | オレンジドット `#FF9900`、サイズ `6×6px`、角丸 `50%` |

##### タイポグラフィ — カラムリンク
| 属性 | 値 |
|---|---|
| フォントサイズ | `16px` |
| フォントウェイト | `400` |
| 行間 | `24px` |
| デフォルトテキスト色 | `#FFFFFFCC`（80%不透明度）|
| ホバー時テキスト色 | `#FFFFFF` |
| リンク間の間隔 | `12px` |

##### オフィス情報
- **会社名**: `font-size: 13px`、`font-weight: 600`、`color: rgba(255,255,255,0.95)`。
- **住所**: `font-size: 13px`、`font-weight: 400`、`line-height: 1.65`、`color: rgba(255,255,255,0.75)`。
- マップピンアイコン色 `#FF9900`、`14×14px`。

##### ボトムバー
- **上ボーダー**: `1px solid rgba(255,255,255,0.08)`。
- **パディング**: `22px 0`。
- **レイアウト**: `flex`、`justify-content: space-between`。
- **著作権表示**: `©2026 Rabiloo. All rights reserved.` — `font-size: 13px`、`color: rgba(255,255,255,0.38)`。
- **ソーシャルアイコン**: 4アイコン（Facebook・LinkedIn・X・YouTube）— 丸いフレーム `34×34px`、ボーダー `1px solid rgba(255,255,255,0.14)`、色 `rgba(255,255,255,0.5)`、ホバー時: 明るいボーダー + 薄い背景 `rgba(255,255,255,0.07)`。

### コアUIコンポーネント定義
* **ユニークバリュープロポジション — UVP（独自価値提案）**: ヒーローセクションに配置される大きな見出し（Headline）。ソリューションが何の問題を・誰のために・なぜ差別化されているかを簡潔に説明します。
* **コール・トゥ・アクション — CTA（アクションボタン）**: UIで最も目立つボタン。ボタン上のテキストは「コンサルティングを申し込む」「技術資料を受け取る」のように明確にアクションを促す表現にします（「お問い合わせ」のような汎用的な表現は避けます）。
* **セクションラベル / ピルラベル（Pill形式のセクション識別子）**: セクション見出しの上に配置する小さなラベルで、コンテンツグループを識別します（例：`コアバリュー`・`導入事例`・`プロセス`）。標準スタイル: フォント **SVN Neue Montreal / Medium 500**、`font-size: 18px`、`line-height: 1.1`、`letter-spacing: 0`、テキスト色 `#111111`、背景 `#F6F6EE`、ボーダー `1px solid #D1D1D1`、Pill型の角丸 `9999px`、パディング `6px 16px`、ドットとテキストの間隔 `8px`。ドットはブランドブルー `#003BBA`、サイズ `7px × 7px`、角丸 `50%`。ラベルのテキストはセンテンスケースで記述（先頭の単語のみ大文字、全体を大文字にしない）。
* **ヒーロービジュアル（Hero Visual：オープニング画像/動画）**: ヒーローセクションの50%の面積を占める画像または動画。アプリケーションのUIインターフェースやソリューションの動作モデルを視覚的に伝えます。
* **ベネフィット vs. フィーチャー（利点と機能の違い）**:
  - *機能（Feature）*: 製品の技術的な説明（例：「AIエージェント自動統合システム」）。
  - *利点（Benefit）*: 顧客にもたらす実際の価値（例：「顧客対応時間を80%自動削減」）。ランディングページは機能よりも**利点**を強調することに重点を置く必要があります。
* **アコーディオン（開閉式コンテンツブロック）**: ユーザーが質問見出し行をクリックすると下の回答が展開されるUIコンポーネント。FAQページをコンパクトにまとめ、ページのスクロール量を減らします。
* **フォームフィールド（入力フォーム）**: ミニマル原則 — 登録フォームの離脱率を下げるため、収集する情報は最大3〜4項目に留めます。

### 共通お問い合わせフォーム（Contact Form）
すべてのランディングページで共通して使用するフォーム。タイトルは **「お問い合わせ」** とします。角丸 `12px` の白いカード形式で表示し、背景は白 `#FFFFFF`、軽いシャドウを付けます。

**フィールド構成（上から順番）：**

| # | フィールド名 | 種類 | 必須 | プレースホルダー |
|---|-----------|------|----------|-------------|
| 1 | **お名前** | テキスト入力 | ✅ 必須（`*`）| *お名前を入力してください* |
| 2 | **電話番号** | テキスト入力 | ✅ 必須（`*`）| *電話番号を入力してください* |
| 3 | **メールアドレス** | メール入力 | ✅ 必須（`*`）| *メールアドレスを入力してください* |
| 4 | **メッセージ** | テキストエリア（4行）| 任意 | *メッセージを入力してください* |

**補足コンポーネント（フィールド下部）：**
- **個人情報同意チェックボックス**（送信前に必ずチェックが必要）:  
  `*Rabilooが私の個人情報を` + ブルー `#003BBA` のリンクテキスト → **個人情報保護方針** + `に従って保存・処理することに同意します`。
- **Cloudflare Turnstile CAPTCHA**: チェックボックスの直下に配置するスパム対策の認証ウィジェット。
- **送信ボタン**: ラベル `送信する`、スタイル `btn-primary`（背景ブルー `#003BBA`、白テキスト）、角丸 `4px`、パディング `16px 32px`。

**バリデーションルール：**
- `*` マーク付きのフィールドは、空欄または不正なフォーマットの場合に入力フィールド下にインラインエラーを表示します。
- メールアドレスは標準正規表現 `^[^\s@]+@[^\s@]+\.[^\s@]+$` に一致する必要があります。
- 電話番号: 8〜11桁の数字、数字のみ入力可。
- 送信前に同意チェックボックスへのチェックが必須です。

---

## 7. Figmaからコーディングへの移行標準（Figma-to-Dev Standards）

FigmaデータをHTMLソースコードに効率的に引き渡せるよう、デザイナーは以下の規則に従って1:1でHTML/CSS構造と互換性のある要素を設定する必要があります：

### Figma オートレイアウトを常に使用すること
オートレイアウトはCSS Flexboxと同等の機能を持ちます。すべてのコンテナへの適用が必須標準です：
* **通常のグループは使用禁止**: レイヤーは通常のグループ（`Ctrl/Cmd + G`）ではなくオートレイアウト（`Shift + A`）でまとめます。
* **リサイズ規約**:
  - *Hug contents*: 内部コンテンツのサイズに自動追従（CSS `width: fit-content` 相当）。
  - *Fill container*: コンテナ全体に広がる（CSS `width: 100%` または `flex-grow: 1` 相当）。
  - *Fixed*: アイコン・アバターなど固定サイズの要素にのみ使用。

### Figma 変数 & スタイルの使用（デザイントークンの同期）
* **Color Variables**: すべてのHEXカラーコードはFigmaの色変数にリンクされている必要があります（例：`primary/500`、`surface/bg`）。
* **Text Styles**: フォント属性・文字サイズ・行間を事前保存済みのテキストスタイルにまとめます（例：`Title/Large`、`Body/Medium`）。

### コンポーネント & バリアントの設計（Components & Variants）
2回以上登場するすべてのコンポーネント（ボタン・入力フィールド・カード・ナビバー）は必ずコンポーネントとして作成します。
* **状態のバリアント（States）**: インタラクション状態のバリアントを完全に作成します。`Default`（通常）・`Hover`（マウスオーバー）・`Focused`（フォーカス）・`Pressed`（押下中）・`Disabled`（無効）の各状態を網羅します。

### Figmaファイル内のページ整理
* **🖼️ Cover**: プロジェクト名・参加メンバー・開発ステータスを示すカバー画像。
* **🎨 Foundations / Design Tokens**: カラーパレット・グリッド・フォントサンプルを表示するページ。
* **⚙️ Components & Specs**: すべてのマスターコンポーネントと状態バリアントを配置する場所。
* **💻 Desktop Screens & 📱 Mobile Screens**: デバイス別に分けた詳細なデザイン画面。
* **❌ Archive / Drafts**: 開発者が間違ったバージョンをコーディングしないよう古いドラフトを保管する場所。

---

## 8. 技術引き渡し & フォルダ構成（Technical Handoff & Code Integration）

デザインの引き渡し（ハンドオフ）時、UIアセットを含むフォルダ構成は、開発者が再構成なしに直接プロジェクトに組み込めるよう合理的に整理されている必要があります。

### 推奨ソースコードフォルダ構成（Folder Structure）
```text
src/
 ├── assets/                 （静的アセット格納）
 │    ├── fonts/             （Neue Montrealフォント .woff2形式）
 │    ├── icons/             （最適化済みのベクター .svg アイコン）
 │    └── images/            （静的画像 .webp、.svg 形式）
 └── styles/                 （デザインシステム定義）
      ├── tokens/            （デザイントークン生データファイル）
      │    ├── colors.css    （プライマリ・ニュートラル・セマンティックカラー）
      │    ├── typography.css（文字サイズ・行間・フォントファミリー）
      │    └── spacing.css   （スペーシングシステム）
      ├── components/        （各コンポーネントの詳細CSS）
      │    ├── button.css    （ボタンスタイル）
      │    ├── card.css      （カードスタイル）
      │    └── input.css     （フォーム入力フィールドスタイル）
      └── main.css           （すべてのCSSファイルをインポートするメインエントリポイント）
```

### 静的アセット管理（Assets Management）
* **フォント**: ページ読み込み容量を最適化するため、常に `.woff2` 形式を優先します。
* **クリーンなSVGアイコン**: SVGコード内の非表示レイヤーやハードコードされた色属性を必ず除去し、開発者がCSSで直接色を制御できるようにします（`color` 属性と `fill="currentColor"` を使用）。
* **画像フォーマット**: LCPスコアを最適化するため、通常の画像には `.png` や `.jpg` の代わりに `.webp` 形式を使用します。

### CSS変数統合の例（styles/tokens/colors.css）
```css
:root {
  /* ブランドカラー */
  --color-primary-500: #003bba;  /* プライマリブルー */
  --color-primary-on: #ffffff;   /* プライマリ背景上のテキスト色 */
  --color-accent-500: #ff9900;   /* アクセントオレンジ */
  --color-accent-on: #111111;    /* アクセント背景上のテキスト色 */

  /* ニュートラルカラー */
  --color-text-primary: #111111;
  --color-text-secondary: #565656;
  --color-text-muted: #c0c0c0;
  --color-border: #d1d1d1;
  --color-bg-tag: #f6f6ee;
  --color-bg-main: #f8f7f5;
  --color-surface: #ffffff;
}
```

### Tailwind CSSを使用するプロジェクトのtailwind.config.js設定
```javascript
module.exports = {
  theme: {
    extend: {
      colors: {
        primary: {
          500: '#003bba',   // プライマリブルー
          on: '#ffffff',
        },
        accent: {
          500: '#ff9900',   // アクセントオレンジ
          on: '#111111',
        },
        neutral: {
          text: {
            primary: '#111111',
            secondary: '#565656',
            muted: '#c0c0c0',
          },
          border: '#d1d1d1',
          bgTag: '#f6f6ee',
          bgMain: '#f8f7f5',
        },
        surface: {
          DEFAULT: '#ffffff',
        }
      },
      spacing: {
        '4px': '4px',
        '8px': '8px',
        '16px': '16px',
        '24px': '24px',
        '32px': '32px',
        '40px': '40px',
        '60px': '60px',
        '80px': '80px',
      },
      borderRadius: {
        'none': '0px',
        'sm': '4px',
        'md': '8px',
        'lg': '16px',
        'xl': '24px',
        'full': '9999px',
      }
    }
  }
}
```
