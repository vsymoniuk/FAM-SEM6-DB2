<?xml version="1.0"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="//data">
        <html>
            <head>
                <title>Task 4</title>
                <style type="text/css">
                    .container {
                        padding: 20px;
                        display: grid;
                        grid-template-columns: repeat(3, 1fr);
                        gap: 20px;

                        font-family: sans-serif;
                    }

                    .good {
                        padding: 20px;
                        border: 2px solid #ccc;
                        background-color: #eaeaea;
                        border-radius: 5px;

                        display: flex;
                        flex-direction: column;
                        align-items: center;
                    }

                    .preview {
                        border-radius: 5px;
                        width: 60%;
                    }

                    .name {
                        font-size: 20px;
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <xsl:for-each select="//good">
                        <div class="good">
                            <img class="preview">
                                <xsl:attribute name="src">
                                    <xsl:value-of select="./image"/>
                                </xsl:attribute>
                            </img>
                            <h1 class="name">
                                <xsl:value-of select="./name"/>
                            </h1>
                            <p class="price">
                                <xsl:value-of select="./price"/>
                            </p>
                        </div>
                    </xsl:for-each>
                </div>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
