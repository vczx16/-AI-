import type { NextPage } from 'next'
import Head from 'next/head'
import Image from 'next/image'
import Dingdong from '../components/dingdong_ai_calculator'
import styles from '../styles/Home.module.css'

const Home: NextPage = () => {
  return (
    <div className={styles.container}>
      <Head>
        <title>Your next generation ai marketing</title>
        <meta name="description" content="Generate branding snippets for your product" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <Dingdong/>
    </div>
  )
}

export default Home
